def get_dashboard_overview_service():
    return {
        "status": "ok",
        "source": "mock-dashboard",
        "carrier": {
            "name": "Emirates",
            "code": "EK",
            "hub": "DXB"
        },
        "hero": {
            "headline": "Potential disruption detected.",
            "summary": "Abnormal delay patterns detected across multiple Middle East routes. Airspace constraints and regional factors are increasing disruption risk over the next operational window.",
            "risk_level": "HIGH",
            "risk_change": "+22 pts / 4h",
            "confidence": 87,
            "watch_window": "4h"
        },
        "command_strip": [
            {"label": "Carrier", "value": "Emirates", "meta": "EK"},
            {"label": "Hub pressure", "value": "Elevated", "meta": "78/100"},
            {"label": "Watch routes", "value": "22 affected", "meta": "+6 today"},
            {"label": "Signal confidence", "value": "87%", "meta": "rising"}
        ],
        "risk_engine": {
            "score": 74,
            "status": "Escalating",
            "change": "+22 pts / 4h",
            "bands": [
                {"label": "Delay spike", "value": 86, "tone": "red"},
                {"label": "Airspace constraint", "value": 72, "tone": "amber"},
                {"label": "DXB congestion", "value": 78, "tone": "red"},
                {"label": "News signal", "value": 54, "tone": "amber"}
            ]
        },
        "flights": [
            {"code": "EK001", "from": "DXB", "to": "LHR", "city": "London Heathrow", "status": "DELAYED", "tone": "red", "delay": "+48m", "risk": "HIGH"},
            {"code": "EK215", "from": "DXB", "to": "LAX", "city": "Los Angeles", "status": "ON TIME", "tone": "green", "delay": "--", "risk": "LOW"},
            {"code": "EK923", "from": "DXB", "to": "CAI", "city": "Cairo", "status": "MONITORING", "tone": "amber", "delay": "+20m", "risk": "MEDIUM"},
            {"code": "EK507", "from": "DXB", "to": "BOM", "city": "Mumbai", "status": "ON TIME", "tone": "green", "delay": "--", "risk": "LOW"},
            {"code": "EK247", "from": "DXB", "to": "SYD", "city": "Sydney", "status": "DELAYED", "tone": "red", "delay": "+1h 35m", "risk": "HIGH"}
        ],
        "regional": {
            "label": "Middle East / Eastern Med.",
            "active_zones": 2,
            "watch_zones": 1,
            "hub_status": "Strained",
            "reroutes": 14
        }
    }