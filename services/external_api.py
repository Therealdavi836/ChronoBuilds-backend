import requests

def fetch_characters_from_api():
    base_url = "https://genshin.jmp.blue/characters"
    response = requests.get(base_url)
    
    if response.status_code == 200:
        character_names = response.json()  # This is a list of strings
        full_characters = []
        
        # We only fetch the first 5 to avoid hitting the API too hard/slowly
        for name in character_names[:5]: 
            char_info = requests.get(f"{base_url}/{name}").json()
            
            full_characters.append({
                "name": char_info.get("name"),
                "element": char_info.get("vision"), # The API uses "vision" for element
                "role": char_info.get("weapon")     # Note: The API doesn't have a "role" field; 
                                                    # usually people use "weapon" or "rarity"
            })
        return full_characters
    return []