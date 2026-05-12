def format_retseptlar(retseptlar):
    if retseptlar:
        text = "--------------------------------"
        for nomi, ingredient, vaqt, murakkablik in retseptlar:
            text += (
                f"\n\n"
                f"🍽 Taom: {nomi}\n\n"
                f"🥕 Ingredientlar: {ingredient}\n"
                f"⏱ Tayyorlash vaqti: {vaqt}\n"
                f"📊 Murakkablik: {murakkablik}\n\n"
                f"--------------------------------"
            )
        return text
    return "❌ Hech qanday retsept topilmadi"
