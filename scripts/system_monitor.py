"""
System Monitoring Script
Monitors CPU, memory, disk usage and system health
"""

import psutil
import json
from datetime import datetime
from typing import Dict
import time

class SystemMonitor:
    """System monitoring and health check"""
    
    def __init__(self, alert_threshold: float = 80.0):
        self.alert_threshold = alert_threshold
        self.metrics = {}
        
    def get_cpu_stats(self) -> Dict:
        """Get CPU statistics"""
        print("[v0] Gathering CPU statistics")
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_count = psutil.cpu_count()
        
        return {
            'usage_percent': cpu_percent,
            'core_count': cpu_count,
            'per_core_usage': psutil.cpu_percent(interval=0.1, percpu=True),
            'alert': cpu_percent > self.alert_threshold
        }
    
    def get_memory_stats(self) -> Dict:
        """Get memory statistics"""
        print("[v0] Gathering memory statistics")
        memory = psutil.virtual_memory()
        
        return {
            'total_gb': round(memory.total / (1024**3), 2),
            'used_gb': round(memory.used / (1024**3), 2),
            'available_gb': round(memory.available / (1024**3), 2),
            'percent': memory.percent,
            'alert': memory.percent > self.alert_threshold
        }
    
    def get_disk_stats(self, path: str = '/') -> Dict:
        """Get disk statistics"""
        print(f"[v0] Gathering disk statistics for {path}")
        disk = psutil.disk_usage(path)
        
        return {
            'total_gb': round(disk.total / (1024**3), 2),
            'used_gb': round(disk.used / (1024**3), 2),
            'free_gb': round(disk.free / (1024**3), 2),
            'percent': disk.percent,
            'alert': disk.percent > self.alert_threshold
        }
    
    def get_network_stats(self) -> Dict:
        """Get network statistics"""
        print("[v0] Gathering network statistics")
        net_io = psutil.net_io_counters()
        
        return {
            'bytes_sent': net_io.bytes_sent,
            'bytes_received': net_io.bytes_recv,
            'packets_sent': net_io.packets_sent,
            'packets_received': net_io.packets_recv
        }
    
    def get_process_info(self, top_n: int = 5) -> Dict:
        """Get top N processes by memory usage"""
        print(f"[v0] Gathering top {top_n} process information")
        processes = []
        
        for proc in psutil.process_iter(['pid', 'name', 'memory_percent']):
            try:
                processes.append({
                    'pid': proc.info['pid'],
                    'name': proc.info['name'],
                    'memory_percent': proc.info['memory_percent']
                })
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        
        # Sort by memory usage
        processes.sort(key=lambda x: x['memory_percent'], reverse=True)
        return {'top_processes': processes[:top_n]}
    
    def generate_health_report(self) -> Dict:
        """Generate comprehensive system health report"""
        print("[v0] Generating system health report")
        timestamp = datetime.now().isoformat()
        
        report = {
            'timestamp': timestamp,
            'cpu': self.get_cpu_stats(),
            'memory': self.get_memory_stats(),
            'disk': self.get_disk_stats(),
            'network': self.get_network_stats(),
            'processes': self.get_process_info(),
            'overall_health': 'HEALTHY'
        }
        
        # Determine overall health
        alerts = sum([
            report['cpu']['alert'],
            report['memory']['alert'],
            report['disk']['alert']
        ])
        
        if alerts >= 2:
            report['overall_health'] = 'CRITICAL'
        elif alerts == 1:
            report['overall_health'] = 'WARNING'
        
        print(f"[v0] System health status: {report['overall_health']}")
        return report
    
    def save_report(self, filepath: str) -> bool:
        """Save health report to file"""
        print(f"[v0] Saving report to {filepath}")
        try:
            report = self.generate_health_report()
            with open(filepath, 'w') as f:
                json.dump(report, f, indent=2)
            print("[v0] Report saved successfully")
            return True
        except Exception as e:
            print(f"[v0] Error saving report: {str(e)}")
            return False
    
    def continuous_monitoring(self, duration_seconds: int = 60, interval: int = 5):
        """Monitor system continuously"""
        print(f"[v0] Starting continuous monitoring for {duration_seconds} seconds")
        start_time = time.time()
        
        while time.time() - start_time < duration_seconds:
            report = self.generate_health_report()
            print(f"[v0] CPU: {report['cpu']['usage_percent']}% | Memory: {report['memory']['percent']}% | Disk: {report['disk']['percent']}%")
            time.sleep(interval)


if __name__ == "__main__":
    monitor = SystemMonitor()
    
    # Generate single report
    report = monitor.generate_health_report()
    print(json.dumps(report, indent=2))
    
    # Save report
    monitor.save_report("system_health_report.json")
    
    # Run continuous monitoring (30 seconds)
    # monitor.continuous_monitoring(duration_seconds=30)
