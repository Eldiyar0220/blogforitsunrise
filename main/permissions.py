from django.contrib.auth.mixins import UserPassesTestMixin


class UserHasPremissionMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.get_object().user == self.request.user