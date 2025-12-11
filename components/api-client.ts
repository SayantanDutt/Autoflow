/**
 * API Client for connecting to Flask backend
 */

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"

export interface SystemHealth {
  timestamp: string
  overall_health: string
  cpu: {
    usage_percent: number
    core_count: number
    alert: boolean
  }
  memory: {
    total_gb: number
    used_gb: number
    percent: number
    alert: boolean
  }
  disk: {
    total_gb: number
    used_gb: number
    percent: number
    alert: boolean
  }
}

export interface DashboardSummary {
  total_tasks: number
  successful_tasks: number
  failed_tasks: number
  system_health: string
  cpu_usage: number
  memory_usage: number
  disk_usage: number
  timestamp: string
}

class APIClient {
  private baseURL: string

  constructor(baseURL: string = API_BASE_URL) {
    this.baseURL = baseURL
  }

  private async request<T>(endpoint: string, options?: RequestInit): Promise<T> {
    const url = `${this.baseURL}${endpoint}`
    console.log("[v0] API Request:", url)

    try {
      const response = await fetch(url, {
        headers: {
          "Content-Type": "application/json",
          ...options?.headers,
        },
        ...options,
      })

      if (!response.ok) {
        throw new Error(`API Error: ${response.status}`)
      }

      return (await response.json()) as T
    } catch (error) {
      console.error("[v0] API Error:", error)
      throw error
    }
  }

  // Health & Status
  async getHealth() {
    return this.request("/api/health")
  }

  async getStatus() {
    return this.request("/api/status")
  }

  // System Monitoring
  async getSystemHealth(): Promise<SystemHealth> {
    return this.request("/api/system/health")
  }

  async getCPUStats() {
    return this.request("/api/system/cpu")
  }

  async getMemoryStats() {
    return this.request("/api/system/memory")
  }

  async getDiskStats(path = "/") {
    return this.request(`/api/system/disk?path=${path}`)
  }

  async getNetworkStats() {
    return this.request("/api/system/network")
  }

  async getProcesses(topN = 5) {
    return this.request(`/api/system/processes?top_n=${topN}`)
  }

  // Data Processing
  async uploadData(file: File) {
    const formData = new FormData()
    formData.append("file", file)

    return this.request("/api/data/upload", {
      method: "POST",
      body: formData,
      headers: {},
    })
  }

  async analyzeFile(filename: string) {
    return this.request(`/api/data/analyze/${filename}`)
  }

  async processData(filepath: string, outputPath: string) {
    return this.request("/api/data/process", {
      method: "POST",
      body: JSON.stringify({ filepath, output_path: outputPath }),
    })
  }

  // File Management
  async listFiles(directory = ".", recursive = false) {
    return this.request(`/api/files/list?directory=${directory}&recursive=${recursive}`)
  }

  async getDirectorySize(directory = ".") {
    return this.request(`/api/files/size?directory=${directory}`)
  }

  async cleanupFiles(directory: string, days: number, extensions?: string[]) {
    return this.request("/api/files/cleanup", {
      method: "POST",
      body: JSON.stringify({
        directory,
        days,
        extensions,
      }),
    })
  }

  async organizeFiles(directory: string) {
    return this.request("/api/files/organize", {
      method: "POST",
      body: JSON.stringify({ directory }),
    })
  }

  async backupFiles(source: string, destination: string) {
    return this.request("/api/files/backup", {
      method: "POST",
      body: JSON.stringify({ source, destination }),
    })
  }

  // History
  async getHistory(limit = 50) {
    return this.request(`/api/history?limit=${limit}`)
  }

  async clearHistory() {
    return this.request("/api/history/clear", {
      method: "POST",
    })
  }

  // Dashboard
  async getDashboardSummary(): Promise<DashboardSummary> {
    return this.request("/api/dashboard/summary")
  }
}

export const apiClient = new APIClient()
