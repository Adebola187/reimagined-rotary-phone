from otree.api import *
import random

Cu = Currency
doc = """
An experiment that presents lottery choices to participants. Choices with varying attributes(options ranging from sure
 payoff to 3 likely payoffs) are presented at random. 
A randomly selected round is picked for payment at the end of the last round.
Read payoff and probability from csv"""


class C(BaseConstants):
    NAME_IN_URL = 'experience'
    questions = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', ]
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = len(questions)
    PARTICIPATION_FEE = cu(8)
    CURR_EX = 0.2
    CHOICES = ['1', '2']


class Subsession(BaseSubsession):
    pass


def shuffle(param):
    random.shuffle(param)
    return param


def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        for p in subsession.get_players():
            round_numbers = list(range(1, C.NUM_ROUNDS + 1))
            random.shuffle(round_numbers)
            task_rounds = dict(zip(C.questions, round_numbers))
            p.participant.task_rounds = task_rounds

    for p in subsession.get_players():
        round_numbers = list(range(1, C.NUM_ROUNDS + 1))
        random.shuffle(round_numbers)
        selected_round = random.randint(1, C.NUM_ROUNDS)
        p.participant.selected_round = selected_round


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    task_rounds = models.IntegerField()
    age = models.IntegerField(label='What is your age?', min=17, max=65)
    gender = models.StringField(
        choices=[['Female', 'Female'], ['Male', 'Male'], ['Prefer not to say', 'Prefer not to say']],
        label='Gender',
        widget=widgets.RadioSelect,
    )
    is_experimented = models.StringField(
        label='How many university experiments have you participated in?',
    )

    education = models.StringField(
        label='Where is your degree primarily located?',
        choices=[['Business School', 'Business School'], ['Arts and Social Sciences', 'Arts and Social Sciences'],
                 ['Life Sciences and Medicines', 'Life Sciences and Medicines'],
                 ['Physical Science', 'Physical Science'],
                 ['Postgraduate Research School', 'Postgraduate Research School'],
                 ['Prefer not to say', 'Prefer not to say']],
        widget=widgets.RadioSelect,
    )

    risk_taking = models.StringField(
        label='How will rate your desire to take risk on a scale 0f 0 to 10? 0 being extremely '
              'unlikely to take risk and 10 being extremely likely',
        choices=[['0', '0'], ['1', '1'], ['2', '2'], ['3', '3'], ['4', '4'], ['5', '5'], ['6', '6'],
                 ['7', '7'], ['8', '8'], ['9', '9'], ['10', '10']],
        widget=widgets.RadioSelectHorizontal,
    )
    Question_1 = models.StringField(
        choices=[['100%', '100%'], ['50%', '50%']],
        label='If you prefer lottery B, what is the chance that you can earn £40',
        widget=widgets.RadioSelect,
    )
    Question_2 = models.StringField(
        choices=[['£40', '£40'], ['£24', '£24'], ['£10', '£10']],
        label='If you choose lottery A, how much can you win?',
        widget=widgets.RadioSelect,
    )
    Question_3 = models.StringField(
        choices=[['£40 and £24', '£40 and £24'], ['£24 and £10', '£24 and £10'], ['£40 and £10', '£40 and £10']],
        label='If you prefer lottery B, what are your payoff possibility?',
        widget=widgets.RadioSelect,
    )

    practice = models.StringField(
        choices=[[
            ["Lottery 1: You have 80% chance to win 4.0 and 20% chance to win 1.0", 4.0, 1.0, '80%', '20%'],
            "Lottery 1"],
            [["Lottery 2: You have 100% chance to win 2.4", 2.4, 2.4, '100%'],
             "Lottery 2"]],
        doc='Players decision', widget=widgets.RadioSelect,
        label='Selection Page: Please select your lottery choice here.'
    )

    q1 = models.StringField(
        choices=shuffle([[1, 'Lottery 1', ], [2, 'Lottery 2']]),
        doc='Players decision',
        widget=widgets.RadioSelect,
        label='Which of these lotteries would you prefer?',
    )
    clicks1 = models.StringField()

    q2 = models.StringField(
        choices=shuffle([[1, 'Lottery 1', ], [2, 'Lottery 2']]),
        doc='Players decision',
        widget=widgets.RadioSelect,
        label='Which of these lotteries would you prefer?'
    )
    clicks2 = models.StringField()

    q3 = models.StringField(
        choices=shuffle([[1, 'Lottery 1', ], [2, 'Lottery 2']]),
        doc='Players decision',
        widget=widgets.RadioSelect,
        label='Which of these lotteries would you prefer?'
    )
    clicks3 = models.StringField()

    q4 = models.StringField(
        choices=shuffle([[1, 'Lottery 1', ], [2, 'Lottery 2']]),
        doc='Players decision',
        widget=widgets.RadioSelect,
        label='Which of these lotteries would you prefer?'
    )
    clicks4 = models.StringField()

    q5 = models.StringField(
        choices=shuffle([[1, 'Lottery 1', ], [2, 'Lottery 2']]),
        doc='Players decision',
        widget=widgets.RadioSelect,
        label='Which of these lotteries would you prefer?'
    )
    clicks5 = models.StringField()

    q6 = models.StringField(
        choices=shuffle([[1, 'Lottery 1', ], [2, 'Lottery 2']]),
        doc='Players decision',
        widget=widgets.RadioSelect,
        label='Which of these lotteries would you prefer?'
    )
    clicks6 = models.StringField()

    q7 = models.StringField(
        choices=shuffle([[1, 'Lottery 1', ], [2, 'Lottery 2']]),
        doc='Players decision',
        widget=widgets.RadioSelect,
        label=' Which of these lotteries would you prefer?'
    )
    clicks7 = models.StringField()

    q8 = models.StringField(
        choices=shuffle([[1, 'Lottery 1', ], [2, 'Lottery 2']]),
        doc='Players decision',
        widget=widgets.RadioSelect,
        label='Which of these lotteries would you prefer?'
    )
    clicks8 = models.StringField()

    q9 = models.StringField(
        choices=shuffle([[1, 'Lottery 1', ], [2, 'Lottery 2']]),
        doc='Players decision',
        widget=widgets.RadioSelect,
        label=' Which of these lotteries would you prefer?'
    )
    clicks9 = models.StringField()

    q10 = models.StringField(
        choices=shuffle([[1, 'Lottery 1', ], [2, 'Lottery 2']]),
        doc='Players decision',
        widget=widgets.RadioSelect,
        label=' Which of these lotteries would you prefer?'
    )
    clicks10 = models.StringField()

    q11 = models.StringField(
        choices=shuffle([[1, 'Lottery 1', ], [2, 'Lottery 2']]),
        doc='Players decision',
        widget=widgets.RadioSelect,
        label='Which of these lotteries would you prefer?'
    )
    clicks11 = models.StringField()

    q12 = models.StringField(
        choices=shuffle([[1, 'Lottery 1', ], [2, 'Lottery 2']]),
        doc='Players decision',
        widget=widgets.RadioSelect,
        label=' Which of these lotteries would you prefer?'
    )
    clicks12 = models.StringField()

    choice_in_round = models.StringField()
    choice = models.IntegerField()
    selected_round = models.StringField()
    random_num_prob = models.IntegerField()
    result = models.FloatField()
    Total = models.FloatField()
    click_1 = models.IntegerField()
    click_2 = models.IntegerField()
    choice_q1 = models.StringField()
    choice_q2 = models.StringField()
    choice_q3 = models.StringField()
    choice_q4 = models.StringField()
    choice_q5 = models.StringField()
    choice_q6 = models.StringField()
    choice_q7 = models.StringField()
    choice_q8 = models.StringField()
    choice_q9 = models.StringField()
    choice_q10 = models.StringField()
    choice_q11 = models.StringField()
    choice_q12 = models.StringField()


# FUNCTIONS
# To define widgets choices as 1 and 2 , i.e Lottery 1 is 1 and Lottery 2 is 2
# def choices_choices(player: Player):
#     # return models.StringField(C.questions)
#     for C.CHOICES in C.questions:
#         player.choices = C.CHOICES
#         C.CHOICES = choices


# To randomize choices
def questions_choice(player: Player):
    import random
    choices = [['1'],
               ['2']
               ]
    random.shuffle(choices)
    return choices


def Q1_choices(player: Player):
    import random
    choices = [['1'],
               ['2']
               ]
    random.shuffle(choices)
    return choices


# PAGES
class DemographicInformation(Page):
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS

    form_model = 'player'
    form_fields = ['age', 'gender', 'is_experimented', 'education', 'risk_taking']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        pass


class Introduction(Page):
    form_model = 'player'
    form_fields = ['Question_1', 'Question_2', 'Question_3']

    @staticmethod
    def error_message(player, values):
        solutions = dict(
            Question_1='50%',
            Question_2='£24',
            Question_3='£40 and £10',
        )
        error_messages = dict()
        for field_name in solutions:
            if values[field_name] != solutions[field_name]:
                error_messages[field_name] = 'Wrong answer'

        return error_messages

    def is_displayed(player: Player):
        return player.round_number == 1

    # create dict for answers to each question
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.session.answers = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9",
                                  10: "10", 11: "11", 12: "12", 13: "13"}
        player.session.previoupage = "Introduction"
        player.session.ROUND_COUNT = 1


class Instruction(Page):
    form_model = 'player'

    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.session.previoupage = "Instruction"


class StartPage(Page):
    form_model = 'player'

    def is_displayed(player: Player):
        return player.round_number == 1


class PartialFeedback(Page):
    form_model = 'player'

    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS


class Practice(Page):
    form_model = 'player'
    form_fields = ['practice']

    @staticmethod
    def is_displayed(player: Player):
        return player.session.previoupage == "Instruction"

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "choice_in_round": player.in_rounds(1, C.NUM_ROUNDS),
            "previous Page": player.session.previoupage
        }

    @staticmethod
    def js_vars(player):
        return dict(percentage1=[4.0, 1.0],
                    percentage2=2.4)

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.session.previoupage = "Practice"
        player.session.answers[13] = player.practice


class Q1(Page):
    form_model = 'player'
    form_fields = ['q1', 'clicks1']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['q1']

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "choice_in_round": player.in_rounds(1, C.NUM_ROUNDS),
            "rounds": f'{player.session.ROUND_COUNT} of {C.NUM_ROUNDS} Questions'
        }

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.choice = player.in_rounds(1, C.NUM_ROUNDS) == player.q1
        choice = {}
        choice[player.q1] = player.in_rounds(1, C.NUM_ROUNDS)
        print(choice)
        if player.q1 == 1:
            answer = {
                "question": "Lottery 1: You have 80% chance to win 4 points and 20% chance to win 0 points",
                "percentages": [80, 20],
                "points": [40, 0],
                "clicks": player.clicks1
            }
        else:
            answer = {
                "question": "Lottery 2: You have 100% chance to win 3.2 points.",
                "percentages": [100],
                "points": [3.2],
                "clicks": player.clicks1
            }
        player.session.answers[1] = answer
        player.session.ROUND_COUNT += 1

    @staticmethod
    def js_vars(player):
        return dict(percentage1=[80, 20],
                    percentage2=[3.2])


class Q2(Page):
    form_model = 'player'
    form_fields = ['q2', 'clicks2']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['q2']

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "choice_in_round": player.in_rounds(1, C.NUM_ROUNDS),
            "rounds": f'{player.session.ROUND_COUNT} of {C.NUM_ROUNDS} Questions'
        }

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q2 == 2:
            answer = {
                "question": 'Lottery 1: You have 10% chance to win 32 points and 90% chance to win 0 points',
                "percentages": [10, 90],
                "points": [32, 0],
                "clicks": player.clicks2
            }
        else:
            answer = {
                "question": "Lottery 2: You have 100% chance to win 3.2 points.",
                "percentages": [100],
                "points": [3.2],
                "clicks": player.clicks2
            }
        player.session.answers[2] = answer
        player.session.ROUND_COUNT += 1

    @staticmethod
    def js_vars(player):
        return dict(percentage1=[32, 0],
                    percentage2=[3.2])


class Q3(Page):
    form_model = 'player'
    form_fields = ['q3', 'clicks3']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['q3']

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "choice_in_round": player.in_rounds(1, C.NUM_ROUNDS),
            "rounds": f'{player.session.ROUND_COUNT} of {C.NUM_ROUNDS} Questions'
        }

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q3 == 1:
            answer = {
                "question": "Lottery 1:You have 14% chance to win 23 points and 86% chance to win 0 points",
                "percentages": [14, 86],
                "points": [23, 0],
                "clicks": player.clicks3
            }
        else:
            answer = {
                "question": "Lottery 2: You have 100% chance to win 3.2 points.",
                "percentages": [100],
                "points": [3.2],
                "clicks": player.clicks3
            }
        player.session.answers[3] = answer
        player.session.ROUND_COUNT += 1

    @staticmethod
    def js_vars(player):
        return dict(percentage1=[23, 0],
                    percentage2=[3.2])


class Q4(Page):
    form_model = 'player'
    form_fields = ['q4', 'clicks4']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['q4']

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "choice_in_round": player.in_rounds(1, C.NUM_ROUNDS),
            "rounds": f'{player.session.ROUND_COUNT} of {C.NUM_ROUNDS} Questions'
        }

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q4 == 1:
            answer = {
                "question": "Lottery 1: You have 98% chance to win 3.26 points and 2% chance to win 0 points",
                "percentages": [98, 2],
                "points": [3.26, 0],
                "clicks": player.clicks4
            }
        else:
            answer = {
                "question": "Lottery 2: You have 100% chance to win 3.2 points.",
                "percentages": [100],
                "points": [3.2],
                "clicks": player.clicks4
            }
        player.session.answers[4] = answer
        player.session.ROUND_COUNT += 1

    @staticmethod
    def js_vars(player):
        return dict(percentage1=[3.26, 0],
                    percentage2=[3.2])


class Q5(Page):
    form_model = 'player'
    form_fields = ['q5', 'clicks5']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['q5']

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "choice_in_round": player.in_rounds(1, C.NUM_ROUNDS),
            "rounds": f'{player.session.ROUND_COUNT} of {C.NUM_ROUNDS} Questions'
        }

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q5 == 1:
            answer = {
                "question": "Lottery 1: You have 20% chance to win 16 points and 80% chance to win 0 points",
                "percentages": [20, 80],
                "points": [16, 0],
                "clicks": player.clicks5
            }
        else:
            answer = {
                "question": "Lottery 2: You have 75% chance to win 2.6 points and 25% to win 5 points",
                "percentages": [75, 25],
                "points": [2.6, 5],
                "clicks": player.clicks5
            }
        player.session.answers[5] = answer
        player.session.ROUND_COUNT += 1

    @staticmethod
    def js_vars(player):
        return dict(percentage1=[16, 0],
                    percentage2=[2.6, 5])


class Q6(Page):
    form_model = 'player'
    form_fields = ['q6', 'clicks6']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['q6']

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "choice_in_round": player.in_rounds(1, C.NUM_ROUNDS),
            "rounds": f'{player.session.ROUND_COUNT} of {C.NUM_ROUNDS} Questions'
        }

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q6 == 1:
            answer = {
                "question": "Lottery 1: You have 84.5% chance to win 3.8 points and 15.5% chance to win 0 points",
                "percentages": [84.5, 15.5],
                "points": [3.8, 0],
                "clicks": player.clicks6
            }
        else:
            answer = {
                "question": "Lottery 2: You have 75% chance to win 3.4 points and 25% to win 2.6 points",
                "percentages": [75, 25],
                "points": [3.4, 2.6],
                "clicks": player.clicks6
            }
        player.session.answers[6] = answer
        player.session.ROUND_COUNT += 1

    @staticmethod
    def js_vars(player):
        return dict(percentage1=[3.8, 0],
                    percentage2=[3.4, 2.6])


class Q7(Page):
    form_model = 'player'
    form_fields = ['q7', 'clicks7']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['q7']

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "choice_in_round": player.in_rounds(1, C.NUM_ROUNDS),
            "rounds": f'{player.session.ROUND_COUNT} of {C.NUM_ROUNDS} Questions'
        }

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q7 == 1:
            answer = {
                "question": "Lottery 1:You have 10% chance to win 24 points, 32% chance to win 2.5 points and 58% chance to win 0 points",
                "percentages": [10, 32, 58],
                "points": [24, 2.5, 0],
                "clicks": player.clicks7
            }
        else:
            answer = {
                "question": "Lottery 2: You have 100% chance to win 3.2 points.",
                "percentages": [100],
                "points": [3.2],
                "clicks": player.clicks7
            }
        player.session.answers[7] = answer
        player.session.ROUND_COUNT += 1

    @staticmethod
    def js_vars(player):
        return dict(percentage1=[24, 2.5, 0],
                    percentage2=[3.2])


class Q8(Page):
    form_model = 'player'
    form_fields = ['q8', 'clicks8']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['q8']

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "choice_in_round": player.in_rounds(1, C.NUM_ROUNDS),
            "rounds": f'{player.session.ROUND_COUNT} of {C.NUM_ROUNDS} Questions'
        }

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q8 == 1:
            answer = {
                "question": "Lottery 1: You have 40% chance to win 6 points; 40% chance to win 2 points and 20% chance to win 0 points",
                "percentages": [40, 40, 20],
                "points": [6, 2, 0],
                "clicks": player.clicks8
            }
        else:
            answer = {
                "question": "Lottery 2: You have 100% chance to win 3.2 points.",
                "percentages": [100],
                "points": [3.2],
                "clicks": player.clicks8
            }
        player.session.answers[8] = answer
        player.session.ROUND_COUNT += 1

    @staticmethod
    def js_vars(player):
        return dict(percentage1=[6, 2, 0],
                    percentage2=[3.2])


class Q9(Page):
    form_model = 'player'
    form_fields = ['q9', 'clicks9']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['q9']

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "choice_in_round": player.in_rounds(1, C.NUM_ROUNDS),
            "rounds": f'{player.session.ROUND_COUNT} of {C.NUM_ROUNDS} Questions'
        }

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q9 == 1:
            answer = {
                "question": "Lottery 1: You have 10% chance to win 30 points, 40% chance to win 0.5 points and 50% chance to win 0 points",
                "percentages": [10, 40, 50],
                "points": [30, 0.5, 0],
                "clicks": player.clicks9
            }
        else:
            answer = {
                "question": "'Lottery 2: You have 50% chance to win 5 points, 50% chance to win 1.4 points",
                "percentages": [50, 50],
                "points": [5, 1.4],
                "clicks": player.clicks9
            }
        player.session.answers[9] = answer
        player.session.ROUND_COUNT += 1

    @staticmethod
    def js_vars(player):
        return dict(percentage1=[30, 0.5, 0],
                    percentage2=[5, 1.4])


class Q10(Page):
    form_model = 'player'
    form_fields = ['q10', 'clicks10']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['q10']

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "choice_in_round": player.in_rounds(1, C.NUM_ROUNDS),
            "rounds": f'{player.session.ROUND_COUNT} of {C.NUM_ROUNDS} Questions'
        }

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q10 == 1:
            answer = {
                "question": "Lottery 1: You have 60% chance to win 5 points; 35% chance to win 0.6 points and 5% chance to win 0 points",
                "percentages": [60, 35, 5],
                "points": [5, 0.6, 0],
                "clicks": player.clicks10
            }
        else:
            answer = {
                "question": "Lottery 2:  You have 50% chance to win 5 points and 50% chance to win 1.4 points",
                "percentages": [50, 50],
                "points": [5, 1.4],
                "clicks": player.clicks10
            }
        player.session.answers[10] = answer
        player.session.ROUND_COUNT += 1

    @staticmethod
    def js_vars(player):
        return dict(percentage1=[5, 0.6, 0],
                    percentage2=[5, 1.4])


class Q11(Page):
    form_model = 'player'
    form_fields = ['q11', 'clicks11']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['q11']

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "choice_in_round": player.in_rounds(1, C.NUM_ROUNDS),
            "rounds": f'{player.session.ROUND_COUNT} of {C.NUM_ROUNDS} Questions'
        }

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q11 == 1:
            answer = {
                "question": "Lottery 1: You have 15% chance to win 16 points; 50% chance to win 1.6 points and 35% chance to win 0 points",
                "percentages": [15, 50, 35],
                "points": [16, 1.6, 0],
                "clicks": player.clicks11
            }
        else:
            answer = {
                "question": "Lottery 2: You have 35% chance to win 5 points; 30% chance to win 2.5 points and 35% chance to win 2 points",
                "percentages": [35, 30, 35],
                "points": [5, 2.5, 2],
                "clicks": player.clicks11
            }
        player.session.answers[11] = answer
        player.session.ROUND_COUNT += 1

    @staticmethod
    def js_vars(player):
        return dict(percentage1=[16, 1.6, 0],
                    percentage2=[5, 2.5, 2])


class Q12(Page):
    form_model = 'player'
    form_fields = ['q12', 'clicks12']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['q12']

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "choice_in_round": player.in_rounds(1, C.NUM_ROUNDS),
            "rounds": f'{player.session.ROUND_COUNT} of {C.NUM_ROUNDS} Questions'
        }

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q12 == 1:
            answer = {
                "question": "Lottery 1: You have 42% chance to win 7.2 points, 40% chance to win 0.45 points and 18% chance to win 0 points",
                "percentages": [42, 40, 18],
                "points": [7.2, 0.45, 0],
                "clicks": player.clicks12
            }
        else:
            answer = {
                "question": "Lottery 2: You have 40% chance to win 4 points; 30% chance to win 3.4 points and 30% chance to win 2 points",
                "percentages": [40, 40, 20],
                "points": [4, 3.4, 2],
                "clicks": player.clicks12
            }
        player.session.answers[12] = answer
        player.session.ROUND_COUNT += 1

    @staticmethod
    def js_vars(player):
        return dict(percentage1=[7.2, 0.45, 0],
                    percentage2=[4, 3.4, 2])

    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        player.session.answers[12] = player.q12
        import random
        participant = player.participant
        # if it's the last round,select a random round from the 10 questions and play the lottery
        # chosen by the participant for the payoff.
        if player.round_number == C.NUM_ROUNDS:
            random_round = random.randint(1, C.NUM_ROUNDS)
            participant.selected_round = random_round
            player.selected_round = str(random_round)
            # player_in_selected_round = player.in_round(random_round)

            return {

                "selected_round": random_round,
            }


def replacechar(self):
    return self.replace("%", "").replace("'", "").replace("[", "").replace("]", "").replace(" ", "")


class RandomRound(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS

    @staticmethod
    def vars_for_template(player: Player):
        probability = random.randint(1, 100)
        random_num_pay = probability
        player.random_num_prob = random_num_pay
        split = player.session.answers[player.participant.selected_round]
        percentages = split["percentages"]
        points = split["points"]
        if len(percentages) == 1:
            answer = points[0]
        elif len(percentages) == 2:
            if probability <= percentages[0]:
                answer = points[0]
            else:
                answer = points[1]
        else:
            if probability <= percentages[0]:
                answer = points[0]
            elif probability <= percentages[1]:
                answer = points[1]
            else:
                answer = points[2]

        result = (float(answer) * 0.2)
        player.payoff = result
        Total_reward = C.PARTICIPATION_FEE + result
        # player.round_for_payment = player.participant.selected_round

        # answer = 32
        return {
            # "answers": player.session.answers[player.participant.selected_round]
            "answer": answer,
            "Total_reward": (round(float(result), 2)) + 8,
            "question": split["question"],
            "participationfee": 8,
            "result": player.payoff,
            "player.payoff": result,
            "info": player.session.answers[player.participant.selected_round],
            "probability_number": random_num_pay,
            "clicks": split["clicks"]
        }


class Results(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS


class PracticeResult(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.session.previoupage == "Practice"

    def vars_for_template(player: Player):
        player.session.previoupage = "PracticeResult"
        probability = random.randint(1, 100)
        random_num_pay = probability
        player.random_num_prob = random_num_pay
        split = player.session.answers[13].split(",")
        if len(split) == 7:
            index = 4
        elif len(split) == 5:
            index = 3
        elif len(split) == 3:
            index = 1
        else:
            index = 5
        if len(split) == 3 and split[3] == "100%":
            answer = split[1].replace("[", "").replace("]", "")
        elif len(split) == 5 and probability <= int(
                split[index].replace("%", "").replace("'", "").replace(" ' ", "").replace("[", "").replace("]", "")):
            answer = split[1].replace("[", "").replace("]", "")
        elif len(split) == 5 and probability >= int(
                split[index].replace("%", "").replace("'", "").replace(" ' ", "").replace("[", "").replace("]", "")):
            answer = split[2].replace("[", "").replace("]", "")
        # elif len(split) == 5 and probability >= (int(replacechar(split[index])) + int(replacechar(split[++index]))):
        #     answer = split[2].replace("[", "").replace("]", "")
        elif len(split) == 7 and probability <= int(
                split[++index].replace("%", "").replace("'", "").replace("[", "").replace("]", "").replace(" ", "")):
            answer = split[1].replace("[", "").replace("]", "")
        elif len(split) == 7 and int(
                split[++4].replace("%", "").replace("'", "").replace("[", "").replace("]", "").replace(" ",
                                                                                                       "")) <= probability <= (
                int(replacechar(split[++4])) + int(replacechar(split[++5]))):
            answer = split[2].replace("[", "").replace("]", "")
        elif len(split) == 7 and probability >= (int(replacechar(split[++4])) + int(replacechar(split[++5]))):
            # >= int(split[+++5].replace("%", "").replace("'", "").replace("'", "").replace("[", "").replace("]","").replace(" ","")):
            answer = split[3].replace("[", "").replace("]", "")
        else:
            answer = 24
        result = (float(answer) * 0.2) + 8
        result = result

        return {
            # "answers": player.session.answers[player.participant.selected_round]
            "answer": answer,
            "question": player.session.answers[player.participant.selected_round].split(",")[0].replace("[",
                                                                                                        "").replace("'",
                                                                                                                    "").replace(
                ";", ","),
            "participationfee": 8,
            "practiceans": player.session.answers[13].split(",")[0].replace("[", "").replace("'", "").replace(";", ","),
            "result": result,
            "info": player.session.answers[player.participant.selected_round],
            "probability_number": random_num_pay,
        }


page_sequence = [Introduction, Instruction, Practice, PracticeResult, StartPage, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9,
                 Q10, Q11, Q12,
                 DemographicInformation, RandomRound]
