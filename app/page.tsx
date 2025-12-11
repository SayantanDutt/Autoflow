"use client"

import { useState } from "react"
import { Dashboard } from "@/components/dashboard"
import { Sidebar } from "@/components/sidebar"
import { Header } from "@/components/header"

export default function Home() {
  const [activeTab, setActiveTab] = useState<"overview" | "tasks" | "analytics" | "settings">("overview")

  return (
    <div className="flex h-screen bg-background">
      <Sidebar activeTab={activeTab} setActiveTab={setActiveTab} />
      <div className="flex-1 flex flex-col overflow-hidden">
        <Header />
        <Dashboard activeTab={activeTab} />
      </div>
    </div>
  )
}
