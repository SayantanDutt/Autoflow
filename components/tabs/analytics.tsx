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
  Legend,
  ResponsiveContainer,
} from "recharts"
import { Card } from "@/components/ui/card"

const monthlyData = [
  { month: "Jan", tasks: 120, duration: 245, efficiency: 85 },
  { month: "Feb", tasks: 132, duration: 221, efficiency: 87 },
  { month: "Mar", tasks: 101, duration: 229, efficiency: 82 },
  { month: "Apr", tasks: 198, duration: 200, efficiency: 90 },
  { month: "May", tasks: 221, duration: 229, efficiency: 92 },
  { month: "Jun", tasks: 250, duration: 210, efficiency: 95 },
]

export function Analytics() {
  return (
    <div className="p-8 space-y-6">
      <div>
        <h2 className="text-2xl font-bold text-foreground">Analytics</h2>
        <p className="text-muted-foreground mt-1">Performance metrics and insights</p>
      </div>

      {/* Monthly Overview */}
      <Card className="bg-card border border-border p-6">
        <h3 className="text-lg font-bold text-foreground mb-4">Monthly Task Execution</h3>
        <ResponsiveContainer width="100%" height={400}>
          <BarChart data={monthlyData}>
            <CartesianGrid strokeDasharray="3 3" stroke="#333" />
            <XAxis dataKey="month" stroke="#999" />
            <YAxis stroke="#999" />
            <Tooltip
              contentStyle={{ backgroundColor: "#1f2937", border: "1px solid #333" }}
              labelStyle={{ color: "#fff" }}
            />
            <Legend />
            <Bar dataKey="tasks" fill="#3b82f6" />
            <Bar dataKey="duration" fill="#06b6d4" />
          </BarChart>
        </ResponsiveContainer>
      </Card>

      {/* Efficiency Trend */}
      <Card className="bg-card border border-border p-6">
        <h3 className="text-lg font-bold text-foreground mb-4">Efficiency Trend</h3>
        <ResponsiveContainer width="100%" height={300}>
          <LineChart data={monthlyData}>
            <CartesianGrid strokeDasharray="3 3" stroke="#333" />
            <XAxis dataKey="month" stroke="#999" />
            <YAxis stroke="#999" />
            <Tooltip
              contentStyle={{ backgroundColor: "#1f2937", border: "1px solid #333" }}
              labelStyle={{ color: "#fff" }}
            />
            <Line type="monotone" dataKey="efficiency" stroke="#8b5cf6" strokeWidth={2} />
          </LineChart>
        </ResponsiveContainer>
      </Card>
    </div>
  )
}
