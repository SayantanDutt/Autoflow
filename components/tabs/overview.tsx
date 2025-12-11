"use client"

import {
  BarChart,
  Bar,
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  PieChart,
  Pie,
  Cell,
} from "recharts"
import { Card } from "@/components/ui/card"
import { Activity, Zap, TrendingUp, Clock } from "lucide-react"

const taskData = [
  { name: "Mon", completed: 12, failed: 2, pending: 3 },
  { name: "Tue", completed: 19, failed: 1, pending: 2 },
  { name: "Wed", completed: 15, failed: 3, pending: 4 },
  { name: "Thu", completed: 22, failed: 0, pending: 1 },
  { name: "Fri", completed: 18, failed: 2, pending: 2 },
  { name: "Sat", completed: 25, failed: 1, pending: 0 },
  { name: "Sun", completed: 20, failed: 2, pending: 1 },
]

const efficiencyData = [
  { name: "Data Processing", value: 45, color: "#3b82f6" },
  { name: "System Monitoring", value: 30, color: "#06b6d4" },
  { name: "File Management", value: 20, color: "#8b5cf6" },
  { name: "Other", value: 5, color: "#6b7280" },
]

const performanceData = [
  { time: "00:00", cpu: 35, memory: 45, disk: 20 },
  { time: "04:00", cpu: 28, memory: 38, disk: 18 },
  { time: "08:00", cpu: 45, memory: 52, disk: 35 },
  { time: "12:00", cpu: 52, memory: 65, disk: 42 },
  { time: "16:00", cpu: 48, memory: 58, disk: 38 },
  { time: "20:00", cpu: 42, memory: 50, disk: 30 },
  { time: "24:00", cpu: 35, memory: 45, disk: 25 },
]

export function Overview() {
  return (
    <div className="p-8 space-y-6">
      {/* Stats Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        <Card className="bg-card border border-border p-6">
          <div className="flex items-start justify-between">
            <div>
              <p className="text-muted-foreground text-sm font-medium">Total Tasks</p>
              <p className="text-3xl font-bold text-foreground mt-2">248</p>
              <p className="text-xs text-green-500 mt-2 flex items-center gap-1">
                <TrendingUp className="w-3 h-3" /> +12% from last week
              </p>
            </div>
            <div className="p-3 bg-primary/10 rounded-lg">
              <Activity className="w-6 h-6 text-primary" />
            </div>
          </div>
        </Card>

        <Card className="bg-card border border-border p-6">
          <div className="flex items-start justify-between">
            <div>
              <p className="text-muted-foreground text-sm font-medium">Completed</p>
              <p className="text-3xl font-bold text-foreground mt-2">218</p>
              <p className="text-xs text-green-500 mt-2">87.9% success rate</p>
            </div>
            <div className="p-3 bg-green-500/10 rounded-lg">
              <Zap className="w-6 h-6 text-green-500" />
            </div>
          </div>
        </Card>

        <Card className="bg-card border border-border p-6">
          <div className="flex items-start justify-between">
            <div>
              <p className="text-muted-foreground text-sm font-medium">Failed</p>
              <p className="text-3xl font-bold text-foreground mt-2">12</p>
              <p className="text-xs text-orange-500 mt-2">Last 7 days</p>
            </div>
            <div className="p-3 bg-orange-500/10 rounded-lg">
              <Activity className="w-6 h-6 text-orange-500" />
            </div>
          </div>
        </Card>

        <Card className="bg-card border border-border p-6">
          <div className="flex items-start justify-between">
            <div>
              <p className="text-muted-foreground text-sm font-medium">Avg. Duration</p>
              <p className="text-3xl font-bold text-foreground mt-2">4.2s</p>
              <p className="text-xs text-blue-500 mt-2">Per task</p>
            </div>
            <div className="p-3 bg-blue-500/10 rounded-lg">
              <Clock className="w-6 h-6 text-blue-500" />
            </div>
          </div>
        </Card>
      </div>

      {/* Charts */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <Card className="lg:col-span-2 bg-card border border-border p-6">
          <h3 className="text-lg font-bold text-foreground mb-4">Weekly Task Performance</h3>
          <ResponsiveContainer width="100%" height={300}>
            <BarChart data={taskData}>
              <CartesianGrid strokeDasharray="3 3" stroke="#333" />
              <XAxis dataKey="name" stroke="#999" />
              <YAxis stroke="#999" />
              <Tooltip
                contentStyle={{ backgroundColor: "#1f2937", border: "1px solid #333" }}
                labelStyle={{ color: "#fff" }}
              />
              <Bar dataKey="completed" stackId="a" fill="#3b82f6" />
              <Bar dataKey="pending" stackId="a" fill="#f59e0b" />
              <Bar dataKey="failed" stackId="a" fill="#ef4444" />
            </BarChart>
          </ResponsiveContainer>
        </Card>

        <Card className="bg-card border border-border p-6">
          <h3 className="text-lg font-bold text-foreground mb-4">Task Distribution</h3>
          <ResponsiveContainer width="100%" height={300}>
            <PieChart>
              <Pie
                data={efficiencyData}
                cx="50%"
                cy="50%"
                innerRadius={60}
                outerRadius={100}
                paddingAngle={2}
                dataKey="value"
              >
                {efficiencyData.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={entry.color} />
                ))}
              </Pie>
              <Tooltip contentStyle={{ backgroundColor: "#1f2937", border: "1px solid #333" }} />
            </PieChart>
          </ResponsiveContainer>
          <div className="mt-4 space-y-2">
            {efficiencyData.map((item) => (
              <div key={item.name} className="flex items-center justify-between text-sm">
                <div className="flex items-center gap-2">
                  <div className="w-2 h-2 rounded-full" style={{ backgroundColor: item.color }} />
                  <span className="text-muted-foreground">{item.name}</span>
                </div>
                <span className="text-foreground font-medium">{item.value}%</span>
              </div>
            ))}
          </div>
        </Card>
      </div>

      {/* System Performance */}
      <Card className="bg-card border border-border p-6">
        <h3 className="text-lg font-bold text-foreground mb-4">System Performance</h3>
        <ResponsiveContainer width="100%" height={300}>
          <LineChart data={performanceData}>
            <CartesianGrid strokeDasharray="3 3" stroke="#333" />
            <XAxis dataKey="time" stroke="#999" />
            <YAxis stroke="#999" />
            <Tooltip
              contentStyle={{ backgroundColor: "#1f2937", border: "1px solid #333" }}
              labelStyle={{ color: "#fff" }}
            />
            <Line type="monotone" dataKey="cpu" stroke="#3b82f6" strokeWidth={2} name="CPU" />
            <Line type="monotone" dataKey="memory" stroke="#06b6d4" strokeWidth={2} name="Memory" />
            <Line type="monotone" dataKey="disk" stroke="#8b5cf6" strokeWidth={2} name="Disk" />
          </LineChart>
        </ResponsiveContainer>
      </Card>
    </div>
  )
}
