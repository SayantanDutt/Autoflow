"""
Flask Backend API for Automation Tool
Connects the web dashboard to Python automation scripts
"""

from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
from datetime import datetime
import json
import os
import sys
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from system_monitor import SystemMonitor
from data_processor import DataProcessor
from file_manager import FileManager

app = Flask(__name__)
CORS(app)

# Store task execution history
execution_history = []
MAX_HISTORY = 100

def add_to_history(task_name: str, status: str, details: dict = None):
    """Add task execution to history"""
    entry = {
        'timestamp': datetime.now().isoformat(),
        'task': task_name,
        'status': status,
        'details': details or {}
    }
    execution_history.append(entry)
    if len(execution_history) > MAX_HISTORY:
        execution_history.pop(0)


# ============== HEALTH & STATUS ENDPOINTS ==============

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    }), 200


@app.route('/api/status', methods=['GET'])
def get_status():
    """Get API status and uptime"""
    return jsonify({
        'api_status': 'running',
        'dashboard_connected': True,
        'scripts_available': ['system_monitor', 'data_processor', 'file_manager'],
        'timestamp': datetime.now().isoformat()
    }), 200


# ============== SYSTEM MONITORING ENDPOINTS ==============

@app.route('/api/system/health', methods=['GET'])
def get_system_health():
    """Get comprehensive system health report"""
    print("[v0] API: Fetching system health report")
    try:
        monitor = SystemMonitor()
        report = monitor.generate_health_report()
        add_to_history('system_health', 'success', {'health': report['overall_health']})
        return jsonify(report), 200
    except Exception as e:
        print(f"[v0] Error in health endpoint: {str(e)}")
        add_to_history('system_health', 'failed', {'error': str(e)})
        return jsonify({'error': str(e)}), 500


@app.route('/api/system/cpu', methods=['GET'])
def get_cpu_stats():
    """Get CPU statistics"""
    print("[v0] API: Fetching CPU stats")
    try:
        monitor = SystemMonitor()
        stats = monitor.get_cpu_stats()
        add_to_history('cpu_stats', 'success')
        return jsonify(stats), 200
    except Exception as e:
        print(f"[v0] Error in CPU endpoint: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/system/memory', methods=['GET'])
def get_memory_stats():
    """Get memory statistics"""
    print("[v0] API: Fetching memory stats")
    try:
        monitor = SystemMonitor()
        stats = monitor.get_memory_stats()
        add_to_history('memory_stats', 'success')
        return jsonify(stats), 200
    except Exception as e:
        print(f"[v0] Error in memory endpoint: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/system/disk', methods=['GET'])
def get_disk_stats():
    """Get disk statistics"""
    print("[v0] API: Fetching disk stats")
    try:
        monitor = SystemMonitor()
        path = request.args.get('path', '/')
        stats = monitor.get_disk_stats(path)
        add_to_history('disk_stats', 'success')
        return jsonify(stats), 200
    except Exception as e:
        print(f"[v0] Error in disk endpoint: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/system/network', methods=['GET'])
def get_network_stats():
    """Get network statistics"""
    print("[v0] API: Fetching network stats")
    try:
        monitor = SystemMonitor()
        stats = monitor.get_network_stats()
        add_to_history('network_stats', 'success')
        return jsonify(stats), 200
    except Exception as e:
        print(f"[v0] Error in network endpoint: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/system/processes', methods=['GET'])
def get_processes():
    """Get top processes by memory usage"""
    print("[v0] API: Fetching top processes")
    try:
        monitor = SystemMonitor()
        top_n = request.args.get('top_n', 5, type=int)
        processes = monitor.get_process_info(top_n)
        add_to_history('processes_info', 'success')
        return jsonify(processes), 200
    except Exception as e:
        print(f"[v0] Error in processes endpoint: {str(e)}")
        return jsonify({'error': str(e)}), 500


# ============== DATA PROCESSING ENDPOINTS ==============

@app.route('/api/data/upload', methods=['POST'])
def upload_data():
    """Upload and process data file"""
    print("[v0] API: Processing uploaded file")
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400

        # Save file
        upload_dir = Path('uploads')
        upload_dir.mkdir(exist_ok=True)
        filepath = upload_dir / file.filename
        file.save(str(filepath))

        # Process file
        processor = DataProcessor(str(filepath))
        processor.load_data()
        processor.clean_data()
        stats = processor.analyze_statistics()

        add_to_history('data_processing', 'success', stats)

        return jsonify({
            'status': 'success',
            'filename': file.filename,
            'statistics': stats
        }), 200

    except Exception as e:
        print(f"[v0] Error in data upload: {str(e)}")
        add_to_history('data_processing', 'failed', {'error': str(e)})
        return jsonify({'error': str(e)}), 500


@app.route('/api/data/analyze/<filename>', methods=['GET'])
def analyze_file(filename):
    """Analyze existing data file"""
    print(f"[v0] API: Analyzing file {filename}")
    try:
        filepath = Path('uploads') / filename
        if not filepath.exists():
            return jsonify({'error': 'File not found'}), 404

        processor = DataProcessor(str(filepath))
        processor.load_data()
        processor.clean_data()
        stats = processor.analyze_statistics()

        add_to_history('data_analysis', 'success')

        return jsonify(stats), 200

    except Exception as e:
        print(f"[v0] Error analyzing file: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/data/process', methods=['POST'])
def process_data():
    """Process data with custom parameters"""
    print("[v0] API: Processing data with custom parameters")
    try:
        data = request.get_json()
        filepath = data.get('filepath')
        output_path = data.get('output_path', 'processed_output.csv')

        if not filepath or not Path(filepath).exists():
            return jsonify({'error': 'File not found'}), 404

        processor = DataProcessor(filepath)
        processor.load_data()
        processor.clean_data()
        processor.save_processed_data(output_path)

        add_to_history('data_process', 'success', {'output': output_path})

        return jsonify({
            'status': 'success',
            'output_file': output_path,
            'message': 'Data processed and saved'
        }), 200

    except Exception as e:
        print(f"[v0] Error processing data: {str(e)}")
        return jsonify({'error': str(e)}), 500


# ============== FILE MANAGEMENT ENDPOINTS ==============

@app.route('/api/files/list', methods=['GET'])
def list_files():
    """List files in directory"""
    print("[v0] API: Listing files")
    try:
        directory = request.args.get('directory', '.')
        recursive = request.args.get('recursive', 'false').lower() == 'true'

        manager = FileManager(directory)
        files = manager.list_files(recursive=recursive)

        add_to_history('list_files', 'success', {'count': len(files)})

        return jsonify({
            'status': 'success',
            'count': len(files),
            'files': files
        }), 200

    except Exception as e:
        print(f"[v0] Error listing files: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/files/size', methods=['GET'])
def get_directory_size():
    """Get directory size"""
    print("[v0] API: Calculating directory size")
    try:
        directory = request.args.get('directory', '.')
        manager = FileManager()
        size_info = manager.get_directory_size(directory)

        add_to_history('directory_size', 'success')

        return jsonify(size_info), 200

    except Exception as e:
        print(f"[v0] Error calculating size: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/files/cleanup', methods=['POST'])
def cleanup_files():
    """Cleanup old files"""
    print("[v0] API: Cleaning up old files")
    try:
        data = request.get_json()
        directory = data.get('directory', '.')
        days = data.get('days', 30)
        extensions = data.get('extensions')

        manager = FileManager()
        deleted_count = manager.cleanup_old_files(directory, days, extensions)

        add_to_history('cleanup_files', 'success', {'deleted': deleted_count})

        return jsonify({
            'status': 'success',
            'deleted_count': deleted_count
        }), 200

    except Exception as e:
        print(f"[v0] Error cleaning up: {str(e)}")
        add_to_history('cleanup_files', 'failed', {'error': str(e)})
        return jsonify({'error': str(e)}), 500


@app.route('/api/files/organize', methods=['POST'])
def organize_files():
    """Organize files by extension"""
    print("[v0] API: Organizing files")
    try:
        data = request.get_json()
        directory = data.get('directory', '.')

        manager = FileManager()
        success = manager.organize_by_extension(directory)

        if success:
            add_to_history('organize_files', 'success')
            return jsonify({'status': 'success', 'message': 'Files organized'}), 200
        else:
            add_to_history('organize_files', 'failed')
            return jsonify({'error': 'Failed to organize files'}), 500

    except Exception as e:
        print(f"[v0] Error organizing: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/files/backup', methods=['POST'])
def backup_files():
    """Backup directory"""
    print("[v0] API: Creating backup")
    try:
        data = request.get_json()
        source = data.get('source')
        destination = data.get('destination')

        if not source or not destination:
            return jsonify({'error': 'Source and destination required'}), 400

        manager = FileManager()
        success = manager.backup_directory(source, destination)

        if success:
            add_to_history('backup_files', 'success')
            return jsonify({'status': 'success', 'message': 'Backup completed'}), 200
        else:
            add_to_history('backup_files', 'failed')
            return jsonify({'error': 'Backup failed'}), 500

    except Exception as e:
        print(f"[v0] Error backing up: {str(e)}")
        return jsonify({'error': str(e)}), 500


# ============== EXECUTION HISTORY ENDPOINTS ==============

@app.route('/api/history', methods=['GET'])
def get_history():
    """Get task execution history"""
    print("[v0] API: Fetching execution history")
    limit = request.args.get('limit', 50, type=int)
    return jsonify({
        'status': 'success',
        'count': len(execution_history),
        'history': execution_history[-limit:]
    }), 200


@app.route('/api/history/clear', methods=['POST'])
def clear_history():
    """Clear execution history"""
    print("[v0] API: Clearing execution history")
    global execution_history
    execution_history.clear()
    return jsonify({'status': 'success', 'message': 'History cleared'}), 200


# ============== DASHBOARD STATS ENDPOINTS ==============

@app.route('/api/dashboard/summary', methods=['GET'])
def get_dashboard_summary():
    """Get dashboard summary data"""
    print("[v0] API: Generating dashboard summary")
    try:
        monitor = SystemMonitor()
        health = monitor.generate_health_report()

        summary = {
            'total_tasks': len(execution_history),
            'successful_tasks': sum(1 for h in execution_history if h['status'] == 'success'),
            'failed_tasks': sum(1 for h in execution_history if h['status'] == 'failed'),
            'system_health': health['overall_health'],
            'cpu_usage': health['cpu']['usage_percent'],
            'memory_usage': health['memory']['percent'],
            'disk_usage': health['disk']['percent'],
            'timestamp': datetime.now().isoformat()
        }

        return jsonify(summary), 200

    except Exception as e:
        print(f"[v0] Error generating summary: {str(e)}")
        return jsonify({'error': str(e)}), 500


# ============== ERROR HANDLERS ==============

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Endpoint not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    print("[v0] Starting Flask API server...")
    print("[v0] API available at http://localhost:8000")
    print("[v0] Dashboard at http://localhost:3000")
    app.run(debug=True, port=8000, host='0.0.0.0')
