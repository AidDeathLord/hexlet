from tests_lesson_1.package_name.capitalize import capitalize


if capitalize('') != '':
    raise Exception('Boom!')

if capitalize('hello') != 'Hello':
    raise Exception('Boom!')

print('Good!')
