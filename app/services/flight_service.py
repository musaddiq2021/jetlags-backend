def get_mock_live_flights():
    return [
        {
            "flight": "EK001",
            "route": "DXB → LHR",
            "status": "Delayed",
            "delay": "+48m",
            "risk": "High"
        },
        {
            "flight": "EK215",
            "route": "DXB → LAX",
            "status": "On Time",
            "delay": "—",
            "risk": "Low"
        },
        {
            "flight": "BA142",
            "route": "DEL → LHR",
            "status": "Monitoring",
            "delay": "+20m",
            "risk": "Medium"
        }
    ]