import json

from mistralai import Mistral

from source.config import MISTRAL_API

class MistralAnalyzer:
    def __init__(self, model: str = 'mistral-large-latest'):
        self.model = model
        self.client = Mistral(api_key=MISTRAL_API)


    @staticmethod
    def _build_prompt(headers: list[str], transcript: str):

        schema = {h: "" for h in headers}
        rule = (
            'Інструкції: \n'
            "- Заповни ТІЛЬКИ ці ключі (не додавай інших).\n"
            "- Якщо даних у транскрипті немає — став порожній рядок \"\".\n"
            "- Якщо є дати — формат YYYY-MM-DD.\n"
            "- Якщо є помилки в словах - виправляй\n"
            "- Відповідь СУВОРО одним JSON-об'єктом."
        )
        return (
            "Є транскрипт телефонної розмови українською.\n"
            "Заповни поля за схемою (ключі мають збігатися 1-в-1):\n\n"
            f"{json.dumps(schema, ensure_ascii=False, indent=2)}\n\n"
            f"{guide}\n\n"
            f'Транскрипт:\n""" {transcript.strip()} """'
        )

    def analyze_to_dict(self, headers: List[str], transcript: str):
        prompt = self._build_prompt(headers, transcript)
        resp = self.client.chat.complete(
            model=self.model,
            messages=[
                {"role": "system", "content": "Відповідай ТІЛЬКИ валідним JSON."},
                {"role": "user", "content": prompt},
            ],
            # JSON-mode у Mistral SDK
            response_format={"type": "json_object"},
            temperature=0.0,
        )
        data = json.loads(resp.choices[0].message.content)
        # гарантуємо порядок/повноту згідно headers
        return {h: ("" if data.get(h) is None else str(data.get(h, ""))) for h in headers}