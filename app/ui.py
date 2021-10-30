from datetime import date
from objectpack.ui import BaseEditWindow, make_combo_box
from m3_ext.ui import all_components as ext


class PermissionWindow(BaseEditWindow):

    """
    Обработка окна Permission
    """

    def _init_components(self):
        super(PermissionWindow, self)._init_components()

        self.name = ext.ExtStringField(
            label='Имя',
            name='name',
            allow_blank=False,
            anchor='100%',
        )
        # Todo: Можно сохраняться через конкретный id
        # self.content_type_id = ext.ExtNumberField(
        #     label='Тип контекста',
        #     name='content_type_id',
        #     allow_blank=False,
        #     anchor='100%',
        #     allow_decimals=False,
        #     allow_negative=False
        # )

        # Todo: Понял что нужно использовать ExtDictSelectField - но как передать туда
        #  параметры для выпадающего меню
        self.content_type_id = ext.ExtDictSelectField(
            label='Тип контекста',
            name='content_type_id',
            value_field='content_type_id',
        )

        self.codename = ext.ExtStringField(
            label='Кодовое имя',
            name='codename',
            allow_blank=False,
            anchor='100%',
        )

    def _do_layout(self):
        super(PermissionWindow, self)._do_layout()
        self.form.items.extend(
            (
                self.name,
                self.content_type_id,
                self.codename
            )
        )

    def set_params(self, params):
        super(PermissionWindow, self).set_params(params)
        self.height = 'auto'


class UserWindow(BaseEditWindow):

    """
    Обработка окна пользователя
    """

    def _init_components(self):
        super(UserWindow, self)._init_components()

        self.password = ext.ExtStringField(
            label='Пароль',
            name='password',
            allow_blank=False,
        )
        self.last_login = ext.ExtDateField(
            label='Последний вход',
            name='last_login',
            start_day=1,
            format='d.m.Y',
            anchor='100%'
        )
        self.is_superuser = ext.ExtCheckBox(
            label='Статус суперпьзователя',
            name='is_superuser',
            anchor='100%',
            checked=False,
        )
        self.username = ext.ExtStringField(
            label='Имя пользователя',
            name='username',
            allow_blank=False,
        )
        self.first_name = ext.ExtStringField(
            label='Имя',
            name='first_name',
        )
        self.last_name = ext.ExtStringField(
            label='Фамилия',
            name='last_name',
        )
        self.email = ext.ExtStringField(
            label='Адрес электронной почты',
            name='email',
        )
        self.is_staff = ext.ExtCheckBox(
            label='Статус персонала',
            name='is_staff',
            checked=False,
        )
        self.is_active = ext.ExtCheckBox(
            label='Активный',
            name='is_active',
            checked=True,
        )
        self.date_joined = ext.ExtDateField(
            label='Дата регистрации',
            name='data_joined',
            start_day=1,
            format='d.m.Y',
            value=date.today().strftime('%d.%m.%Y'),
            anchor='100%'
        )

    def _do_layout(self):
        super(UserWindow, self)._do_layout()
        self.form.items.extend(
            (
                self.password,
                self.last_login,
                self.is_superuser,
                self.username,
                self.first_name,
                self.last_name,
                self.email,
                self.is_staff,
                self.is_active,
                self.date_joined,
            )
        )

    def set_params(self, params):
        super(UserWindow, self).set_params(params)
        self.height = 'auto'

