"use client"

import { Bell, User, Settings } from "lucide-react"

export function Header() {
  return (
    <div className="h-16 bg-background border-b border-border flex items-center justify-between px-6">
      <div>
        <h2 className="text-2xl font-bold text-foreground">Automation Dashboard</h2>
      </div>

      <div className="flex items-center gap-4">
        <div className="flex items-center gap-2 bg-sidebar px-4 py-2 rounded-lg">
          <div className="w-2 h-2 bg-green-500 rounded-full animate-pulse"></div>
          <span className="text-sm text-muted-foreground">System Active</span>
        </div>

        <button className="p-2 hover:bg-sidebar rounded-lg transition-colors">
          <Bell className="w-5 h-5 text-muted-foreground" />
        </button>

        <button className="p-2 hover:bg-sidebar rounded-lg transition-colors">
          <Settings className="w-5 h-5 text-muted-foreground" />
        </button>

        <button className="p-2 hover:bg-sidebar rounded-lg transition-colors">
          <User className="w-5 h-5 text-muted-foreground" />
        </button>
      </div>
    </div>
  )
}
