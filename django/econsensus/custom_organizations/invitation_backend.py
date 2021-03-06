from organizations.backends.defaults import InvitationBackend

class CustomInvitationBackend(InvitationBackend):
    """
    Customise django-organizations' default InvitationBackend so that we can
    provide our own body and subject templates for the emails.
    """
    invitation_subject = 'email/invitation_subject.txt'
    invitation_body = 'email/invitation_body.html'
    reminder_body = 'email/reminder_body.html'
