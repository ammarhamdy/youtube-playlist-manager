from view import main_view
from control.main_controller import init_controller


if __name__ == "__main__":
    main_view = main_view.MainView()
    init_controller(main_view)
    main_view.show()
