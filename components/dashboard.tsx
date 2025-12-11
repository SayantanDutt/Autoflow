"use client"

import { Overview } from "./tabs/overview"
import { Tasks } from "./tabs/tasks"
import { Analytics } from "./tabs/analytics"
import { Settings } from "./tabs/settings"

interface DashboardProps {
  activeTab: string
}

export function Dashboard({ activeTab }: DashboardProps) {
  return (
    <div className="flex-1 overflow-auto bg-background">
      {activeTab === "overview" && <Overview />}
      {activeTab === "tasks" && <Tasks />}
      {activeTab === "analytics" && <Analytics />}
      {activeTab === "settings" && <Settings />}
    </div>
  )
}
