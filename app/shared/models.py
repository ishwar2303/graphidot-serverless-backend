class FeedbackModel:
    def __init__(self):
        self.rating: str = None
        self.comment: str = None
        self.captchaToken: str = None

class ContactUsModel:
    def __init__(self):
        self.firstName: str = None
        self.lastName: str = None
        self.email: str = None
        self.contact: str = None
        self.customerMessage1: str = None
        self.captchaToken: str = None

class ReportBugModel:
    def __init__(self):
        self.url = None
        self.details = None
        self.browser = None
        self.operatingSystem = None
        self.captchaToken = None

class CustomerReviewModel:
    def __init__(self):
        self.firstName = None
        self.lastName = None
        self.email = None
        self.serviceName = None
        self.comment = None
        self.overallRating = None
        self.refer = None
        self.expectation = None
        self.subscribe = None
        self.captchaToken = None