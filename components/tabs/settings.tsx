"use client"

import { Card } from "@/components/ui/card"
import { Save, Plus, Trash2 } from "lucide-react"
import { useState } from "react"

export function Settings() {
  const [settings, setSettings] = useState({
    apiUrl: "http://localhost:8000",
    refreshInterval: 30,
    emailNotifications: true,
    logRetention: 30,
  })

  const [integrations, setIntegrations] = useState([
    { id: 1, name: "Slack", status: "connected" },
    { id: 2, name: "AWS S3", status: "connected" },
    { id: 3, name: "Email", status: "pending" },
  ])

  return (
    <div className="p-8 space-y-6 max-w-2xl">
      <div>
        <h2 className="text-2xl font-bold text-foreground">Settings</h2>
        <p className="text-muted-foreground mt-1">Configure your automation environment</p>
      </div>

      {/* General Settings */}
      <Card className="bg-card border border-border p-6">
        <h3 className="text-lg font-bold text-foreground mb-4">General Settings</h3>
        <div className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-foreground mb-2">API URL</label>
            <input
              type="text"
              value={settings.apiUrl}
              onChange={(e) => setSettings({ ...settings, apiUrl: e.target.value })}
              className="w-full bg-sidebar border border-border rounded-lg px-3 py-2 text-foreground focus:outline-none focus:border-primary"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-foreground mb-2">Refresh Interval (seconds)</label>
            <input
              type="number"
              value={settings.refreshInterval}
              onChange={(e) => setSettings({ ...settings, refreshInterval: Number.parseInt(e.target.value) })}
              className="w-full bg-sidebar border border-border rounded-lg px-3 py-2 text-foreground focus:outline-none focus:border-primary"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-foreground mb-2">Log Retention (days)</label>
            <input
              type="number"
              value={settings.logRetention}
              onChange={(e) => setSettings({ ...settings, logRetention: Number.parseInt(e.target.value) })}
              className="w-full bg-sidebar border border-border rounded-lg px-3 py-2 text-foreground focus:outline-none focus:border-primary"
            />
          </div>

          <div className="flex items-center gap-3">
            <input
              type="checkbox"
              checked={settings.emailNotifications}
              onChange={(e) => setSettings({ ...settings, emailNotifications: e.target.checked })}
              className="w-4 h-4 rounded"
            />
            <label className="text-sm font-medium text-foreground">Enable Email Notifications</label>
          </div>

          <button className="flex items-center gap-2 bg-primary text-white px-4 py-2 rounded-lg hover:bg-primary-dark transition-colors">
            <Save className="w-4 h-4" />
            Save Settings
          </button>
        </div>
      </Card>

      {/* Integrations */}
      <Card className="bg-card border border-border p-6">
        <div className="flex items-center justify-between mb-4">
          <h3 className="text-lg font-bold text-foreground">Integrations</h3>
          <button className="flex items-center gap-2 bg-primary text-white px-3 py-1 rounded-lg text-sm hover:bg-primary-dark transition-colors">
            <Plus className="w-4 h-4" />
            Add Integration
          </button>
        </div>

        <div className="space-y-3">
          {integrations.map((integration) => (
            <div key={integration.id} className="flex items-center justify-between p-3 bg-sidebar rounded-lg">
              <div>
                <p className="font-medium text-foreground">{integration.name}</p>
                <p
                  className={`text-xs mt-1 ${
                    integration.status === "connected" ? "text-green-500" : "text-yellow-500"
                  }`}
                >
                  {integration.status.charAt(0).toUpperCase() + integration.status.slice(1)}
                </p>
              </div>
              <button className="p-2 hover:bg-card rounded-lg transition-colors">
                <Trash2 className="w-4 h-4 text-red-500" />
              </button>
            </div>
          ))}
        </div>
      </Card>
    </div>
  )
}
