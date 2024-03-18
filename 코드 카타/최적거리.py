
start = input()
end = input()

graph = {
    "Seoul": {"Wonju": 88, "Daejeon": 140, "Gwangju": 270, "Sokcho": 168},
    "Wonju": {"Seoul": 88, "Sokcho": 110, "Daejeon": 120, "Busan": 260},
    "Daejeon": {"Wonju": 120, "Seoul": 140, "Gwangju": 200, "Busan": 200},
    "Gwangju": {"Daejeon": 200, "Seoul": 270, "Busan": 200},
    "Busan": {"Gwangju": 200, "Daejeon": 200, "Wonju": 200, "Sokcho": 340},
    "Sokcho": {"Seoul": 168, "Wonju": 110, "Busan": 340},
}
