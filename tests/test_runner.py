from types import FunctionType, ModuleType
from os import path, listdir
from importlib.util import spec_from_file_location, module_from_spec

def import_module_by_path(module_path: str):
    '''
        Spec from file -> Module from file -> execute module using spec.
    '''
    module_name = module_path.split(path.sep)[-1][:-3]  # Provide a custom name for the module
    spec = spec_from_file_location(module_name, module_path)
    custom_module = module_from_spec(spec)
    spec.loader.exec_module(custom_module)

    return custom_module


def get_current_folder() -> str :
    return path.sep.join(__file__.split(path.sep)[:-1])


def run_tests(module: ModuleType):
    results = {}
    # Run all methods with *_test
    for k, v in module.__dict__.items():
        # It is instance of FunctionType is key here :)-:
        if k.endswith('_test') and isinstance(v, (FunctionType)):
            try:
                v()
                results[k] = 'Pass'
            except Exception as e:
                results[k] = 'Fail: ' + str(e)
    return results


if __name__ == '__main__':
    '''
        This will run all the functions matching *_test in all the files in current folder.
    '''

    # For all files in current folder
    current_folder = get_current_folder()

    for file in listdir(current_folder):
        file = path.join(current_folder, file)

        if path.isfile(file) and file.endswith('test.py'):
            custom_module = import_module_by_path(file)

            results = run_tests(custom_module)
            print('Results for file: ' + file)
            for k, v in results.items():
                print(f'{k} - {v}')
            print()



