import datetime

from django.core.management.base import BaseCommand

from polls.models import Question, Choice


class Command(BaseCommand):
    def add_poll(self, question, pub_date, choices):
        question = Question(question_text=question, pub_date=pub_date)
        question.save()

        for choice in choices:
            choice = Choice(question=question, choice_text=choice)
            choice.save()

    def handle(self, *args, **options):
        current_date = datetime.datetime.now() - datetime.timedelta(days=1)
        self.add_poll(
            "What is the brand of the CPU in you computer?",
            current_date,
            ["Intel", "AMD", "Other"],
        )

        current_date = current_date + datetime.timedelta(minutes=1)
        self.add_poll(
            "What is the brand of the GPU in you computer?",
            current_date,
            ["Intel", "Nvidia", "AMD", "Other"],
        )

        current_date = current_date + datetime.timedelta(minutes=1)
        self.add_poll(
            "Who is your favorite Avenger?",
            current_date,
            [
                "Iron Man",
                "Thor",
                "Hulk",
                "Captain America",
                "Ant-Man",
                "Hawkeye",
                "Black Panther",
                "Scarlet Witch",
                "Other",
            ],
        )

        current_date = current_date + datetime.timedelta(minutes=1)
        self.add_poll(
            "What python web framework are you using right now?",
            current_date,
            ["Django", "Flask", "FastAPI", "Others"],
        )

        current_date = current_date + datetime.timedelta(minutes=1)
        self.add_poll(
            "What programming language are you learning right now?",
            current_date,
            ["Fortran", "Cobol", "Haskell", "Rust", "Zig", "Others"],
        )
