from config import Config
from module1.module1_class1 import Module1Class1
from module1.module1_class2 import Module1Class2
from module2.module2_class1 import Module2Class1
from module2.module2_class2 import Module2Class2
from module3.module3_class1 import Module3Class1
from module3.module3_class2 import Module3Class2

def main():
    config = Config()

    config.set_dynamic_param('auth_token', '12345')
    config.set_dynamic_param('current_user', 'johndoe')
    config.set_dynamic_param('session_id', 'abc123')

    module1_class1 = Module1Class1(config)
    module1_class1.connect_db()
    module1_class1.show_user()

    module1_class2 = Module1Class2(config)
    module1_class2.log_message("This is a log message.")

    module2_class1 = Module2Class1(config)
    module2_class1.authenticate()

    module2_class2 = Module2Class2(config)
    module2_class2.get_max_connections()

    module3_class1 = Module3Class1(config)
    module3_class1.get_db_host()

    module3_class2 = Module3Class2(config)
    module3_class2.set_session_id('xyz789')

if __name__ == "__main__":
    main()
