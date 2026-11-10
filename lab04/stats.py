def parse_record(line: str) -> dict:
    parts = line.split(";")          
    if len(parts) != 3:              
        raise ValueError("нужно ровно три поля")

    city = parts[0].strip()          
    temp_text = parts[1].strip()
    date = parts[2].strip()

    if city == "" or date == "":
        raise ValueError("город или дата пустые")

    try:
        temperature = float(temp_text.replace(",", "."))   
    except ValueError:
        raise ValueError("температура не число")

    return {"city": city, "temperature": temperature, "date": date}

def read_valid(lines: list[str]) -> list[dict]:
    result = []
    for line in lines:
        if line.strip() == "":       
            continue
        try:
            result.append(parse_record(line))
        except ValueError:           
            continue
    return result

def average_by_city(records: list[dict]) -> dict:
    total = {}
    count = {}
    for rec in records:
        city = rec["city"]
        total[city] = total.get(city, 0) + rec["temperature"]
        count[city] = count.get(city, 0) + 1

    result = {}
    for city in total:
        result[city] = round(total[city] / count[city], 1)
    return result


def warmest_city(records: list[dict]) -> str:
    averages = average_by_city(records)
    return min(averages, key=lambda c: (-averages[c], c))


    
