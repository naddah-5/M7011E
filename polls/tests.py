import datetime

from django.http import HttpResponse
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question

# Create your tests here.

def create_question(new_question_text: str, offset_days: int) -> Question:
    """
    Creates a question with the given question_text and published 
    the given number of 'days' offset to now.
    """
    time: datetime.datetime = timezone.now() + datetime.timedelta(days=offset_days)
    return Question.objects.create(question_text=new_question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self) -> None:
        """
        If no questions exist, an appropiate message is displayed.
        """
        response: HttpResponse = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self) -> None:
        """
        Question with a pub_date in the past are displayed on the index page.
        """
        create_question(new_question_text="Past question.", offset_days=-30)
        response: HttpResponse = self.client.get(reverse('polls:index'))
        resp: list[str] = []
        for query in response.context['latest_question_list']:
            resp.append(str(query))
        self.assertEqual(
            resp,
            ['Past question.']
        )

    def test_future_question(self) -> None:
        """
        Questions with a pub_date in the future aren't displayed on the index page.
        """
        create_question(new_question_text="Future question.", offset_days=30)
        response : HttpResponse = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self) -> None:
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time: datetime.datetime = timezone.now() + datetime.timedelta(days=30)
        future_question: Question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self) -> None:
        """
        was_published_recently() returns False for questions whose pub_date is older
        than one day.
        """
        not_recent: datetime.datetime = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question: Question = Question(pub_date = not_recent)
        self.assertIs(old_question.was_published_recently(), False)

    def test_future_question_and_past_question(self) -> None:
        """
        Even if both past and future question exist, only past questions are displayed.
        """
        create_question(new_question_text="Past question.", offset_days=-30)
        create_question(new_question_text="Future question.", offset_days=30)
        response: HttpResponse = self.client.get(reverse('polls:index'))
        resp: list[str] = []
        for query in response.context['latest_question_list']:
            resp.append(str(query))
        self.assertEqual(
            resp,
            ['Past question.']
        )

    def test_two_past_questions(self) -> None:
        """
        The questions index page may displa multiple questions.
        """
        create_question(new_question_text="Past question one.", offset_days=-30)
        create_question(new_question_text="Past question two.", offset_days=-5)
        response: HttpResponse = self.client.get(reverse('polls:index'))
        resp: list[str] = []
        for query in response.context['latest_question_list']:
            resp.append(str(query))
        self.assertEqual(
            resp,
            ['Past question two.', 'Past question one.']
        )
        

    def test_was_published_recently_with_recent_question(self) -> None:
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        very_recent: datetime.datetime = timezone.now() - datetime.timedelta(minutes=5)
        recent: datetime.datetime = timezone.now() - datetime.timedelta(hours=12)
        pretty_recent: datetime.datetime = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)

        very_recent_question: Question = Question(pub_date=very_recent)
        recent_question: Question = Question(pub_date=recent)
        pretty_recent_question: Question = Question(pub_date=pretty_recent)

        self.assertIs(very_recent_question.was_published_recently(), True)
        self.assertIs(recent_question.was_published_recently(), True)
        self.assertIs(pretty_recent_question.was_published_recently(), True)


# currently on page 53
class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future returns a 404 not found.
        """
        future_question: Question = create_question(new_question_text='Future question', offset_days=30)
        # Note that the id has to be in the form of a string for djangos reverse() function.
        future_question_id: str = str(future_question.id)
        url: str = reverse('polls:detail', args=(future_question_id))
        response: HttpResponse = self.client.get(url)
        self.assertEqual(response.status_code, 404)