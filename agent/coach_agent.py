from agent.groq_client import GroqClient

class CoachAgent:
    def __init__(self):
        self.client = GroqClient()
        self.system_prompt = """
You are a multi-role AI Fitness Coach system operating inside a production-grade Gym Trainer application.
You must behave like a professional team consisting of:
- Fitness Profile Analyst 📊
- Certified Personal Trainer 🏋️
- Sports Nutrition Specialist 🥗
- Motivation Coach 🔥

CORE RULES:
1. Always prioritize safety: No extreme dieting, no harmful workout advice, no unrealistic transformations.
2. Always personalize based on: Age, Weight, Fitness level, Goal, Available days, Equipment, and Meals per day.
3. Keep output: Professional and structured. Use EMOJIS sparingly (only for key headers) to maintain a clean look.

STRICT OUTPUT FORMAT FOR PLANS:
### 🧑 PROFILE SUMMARY
(2-4 lines summarizing the user)

---
### 💪 WEEKLY WORKOUT PLAN
(Day-by-day plan with exercise names, sets, reps)

---
### 🥗 NUTRITION PLAN
- Breakfast
- Lunch
- Dinner
- Healthy snacks
- Hydration advice

---
### 📈 PROGRESS STRATEGY
(How to improve in 4 weeks, what to track)

---
### 🔥 MOTIVATION MESSAGE
(2-4 lines max)

CHATBOX RULES:
- Use emojis sparingly and strategically.
- Provide guidance in POINT-WISE format rather than long sentences.
- Stay consistent with the user's generated plan.
"""

    def generate_plan(self, profile):
        user_input = f"""
USER PROFILE:
- Age: {profile['age']}
- Weight: {profile['weight']} kg
- Level: {profile['level']}
- Goal: {profile['goal']}
- Days per week: {profile['days']}
- Meals per day: {profile['meals']}
- Equipment: {profile['equipment']}
- Injury Notes: {profile.get('notes', 'None')}
- Pain Level: {profile.get('pain_level', 0)}/10
"""
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_input}
        ]
        return self.client.get_completion(messages)

    def chat_response(self, chat_history, user_query, profile):
        system_context = f"You are the same Fitness Coach team. Context: User is {profile['age']}yo, {profile['weight']}kg, {profile['level']} level, aiming for {profile['goal']}. Injury: {profile.get('notes', 'None')} (Pain: {profile.get('pain_level', 0)}/10). Respond in points with subtle emoji usage."
        messages = [{"role": "system", "content": system_context}]
        messages.extend(chat_history)
        messages.append({"role": "user", "content": user_query})
        
        return self.client.get_completion(messages)

    def stream_chat_response(self, chat_history, user_query, profile):
        system_context = f"You are the same Fitness Coach team. Context: User is {profile['age']}yo, {profile['weight']}kg, {profile['level']} level, aiming for {profile['goal']}. Injury: {profile.get('notes', 'None')} (Pain: {profile.get('pain_level', 0)}/10). Respond in points with subtle emoji usage."
        messages = [{"role": "system", "content": system_context}]
        messages.extend(chat_history)
        messages.append({"role": "user", "content": user_query})
        
        return self.client.stream_completion(messages)
