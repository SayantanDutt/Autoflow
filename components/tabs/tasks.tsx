"use client"

import { Card } from "@/components/ui/card"
import { Play, Pause, Trash2, Plus, CheckCircle, AlertCircle, Clock } from "lucide-react"
import { useState } from "react"

const SAMPLE_TASKS = [
  {
    id: 1,
    name: "Daily Data Backup",
    description: "Backup database to S3",
    status: "running",
    progress: 65,
    nextRun: "2 hours",
  },
  {
    id: 2,
    name: "Log Cleanup",
    description: "Remove logs older than 30 days",
    status: "completed",
    progress: 100,
    lastRun: "1 hour ago",
  },
  {
    id: 3,
    name: "System Health Check",
    description: "Monitor CPU, Memory, Disk usage",
    status: "scheduled",
    progress: 0,
    nextRun: "30 minutes",
  },
  {
    id: 4,
    name: "Email Report Generation",
    description: "Generate and send daily reports",
    status: "failed",
    progress: 0,
    error: "Connection timeout",
  },
  {
    id: 5,
    name: "Cache Optimization",
    description: "Clear and optimize cache",
    status: "idle",
    progress: 0,
    nextRun: "Tomorrow",
  },
]

export function Tasks() {
  const [tasks, setTasks] = useState(SAMPLE_TASKS)

  const getStatusColor = (status: string) => {
    switch (status) {
      case "running":
        return "text-blue-500"
      case "completed":
        return "text-green-500"
      case "failed":
        return "text-red-500"
      case "scheduled":
        return "text-yellow-500"
      default:
        return "text-gray-500"
    }
  }

  const getStatusBg = (status: string) => {
    switch (status) {
      case "running":
        return "bg-blue-500/10"
      case "completed":
        return "bg-green-500/10"
      case "failed":
        return "bg-red-500/10"
      case "scheduled":
        return "bg-yellow-500/10"
      default:
        return "bg-gray-500/10"
    }
  }

  return (
    <div className="p-8 space-y-6">
      {/* Header with Add Button */}
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-bold text-foreground">Automation Tasks</h2>
          <p className="text-muted-foreground mt-1">Manage and monitor your automation scripts</p>
        </div>
        <button className="flex items-center gap-2 bg-primary text-white px-4 py-2 rounded-lg hover:bg-primary-dark transition-colors">
          <Plus className="w-4 h-4" />
          Add New Task
        </button>
      </div>

      {/* Tasks List */}
      <div className="space-y-3">
        {tasks.map((task) => (
          <Card key={task.id} className="bg-card border border-border p-6 hover:border-primary/50 transition-colors">
            <div className="flex items-start justify-between gap-4">
              <div className="flex-1">
                <div className="flex items-center gap-3 mb-2">
                  <h3 className="font-bold text-foreground text-lg">{task.name}</h3>
                  <span
                    className={`px-3 py-1 rounded-full text-xs font-medium ${getStatusBg(task.status)} ${getStatusColor(task.status)}`}
                  >
                    {task.status.charAt(0).toUpperCase() + task.status.slice(1)}
                  </span>
                </div>
                <p className="text-muted-foreground text-sm mb-3">{task.description}</p>

                {/* Progress Bar */}
                {task.progress > 0 && (
                  <div className="w-full bg-sidebar rounded-full h-2 overflow-hidden">
                    <div
                      className="bg-primary h-full transition-all duration-300"
                      style={{ width: `${task.progress}%` }}
                    />
                  </div>
                )}

                {/* Timing Info */}
                <div className="mt-3 flex items-center gap-4 text-xs text-muted-foreground">
                  {task.nextRun && (
                    <span className="flex items-center gap-1">
                      <Clock className="w-3 h-3" />
                      Next: {task.nextRun}
                    </span>
                  )}
                  {task.error && (
                    <span className="flex items-center gap-1 text-red-500">
                      <AlertCircle className="w-3 h-3" />
                      {task.error}
                    </span>
                  )}
                  {task.lastRun && (
                    <span className="flex items-center gap-1">
                      <CheckCircle className="w-3 h-3" />
                      Last: {task.lastRun}
                    </span>
                  )}
                </div>
              </div>

              {/* Action Buttons */}
              <div className="flex items-center gap-2">
                {task.status === "running" ? (
                  <button className="p-2 bg-yellow-500/10 text-yellow-500 rounded-lg hover:bg-yellow-500/20 transition-colors">
                    <Pause className="w-4 h-4" />
                  </button>
                ) : (
                  <button className="p-2 bg-green-500/10 text-green-500 rounded-lg hover:bg-green-500/20 transition-colors">
                    <Play className="w-4 h-4" />
                  </button>
                )}
                <button className="p-2 bg-red-500/10 text-red-500 rounded-lg hover:bg-red-500/20 transition-colors">
                  <Trash2 className="w-4 h-4" />
                </button>
              </div>
            </div>
          </Card>
        ))}
      </div>
    </div>
  )
}
