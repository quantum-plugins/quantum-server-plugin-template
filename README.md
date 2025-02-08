# Quantum Server Plugin

To create a plugin for [local-quantum-server](https://github.com/Dpbm/local-quantum-server), start by using this template and then follow the steps below.

## Setup your plugin

1. setup your `requirements.txt`

In your plugin, you'll probably need some external dependencies, like `qiskit`, `cirq`, `pennylane`, `numpy`, etc. List every required dependency inside the [requirements.txt file](./requirements.txt), line by line.

2. create a virtual environment

To keep your work clean, make sure to use a virtual environment, this way your work won't get conflicted with pre-installed system dependencies.

Also, using managers allows you to easily change python versions. By default I'm using the `python 3.12.8`, however it maybe not the perfect match for your plugin. So remember to change it and explicit it on your project.

3. add your code

After that update the folder [[your plugin name]](./[your%20plugin%20name]/) to your plugin name and start adding your code.

Inside `[your plugin name]` directory, you'll find some files:

- [interface.py](./[your%20plugin%20name]/interface.py): that's the file that creates the abstract class `Plugin`, which your project must use to ensure the correct usability. Don't change this file. Only `import` the `types`, `classes` and `functions` you need.
- [plugin.py](./[your%20plugin%20name]/plugin.py): that's the plugin starting point. In it, you may list the backends names your plugin can access. Also, you need to add some logic to handle the user input inside the `execute` method. By default, the class uses a decorator (`@check_backend`) to ensure that only defined backends can be accessed. However, you're free to implement your logic and do further checks. 
- [tests](./[your%20plugin%20name]/tests/): Inside this folder, you can add all your tests. They are not mandatory, but is a good practice to make your project safer to new changes.

Besides that, you're allowed to add new files and create your structure. However, keep in mind that, more complex projects may need additional configurations on either [setup.py](./setup.py) or [pyproject.toml](./pyproject.toml).

Also, you need to ensure the correct handling of the `result_types`, the possible inputs are: `'quasi_dist', 'counts', 'expval'`.

4. update the [setup.py](./setup.py)

With your code done, start adding your info to [setup.py](./setup.py). If you have a more complex structure, you may need to add more configurations to that, so remember to check the [setuptools guide](https://setuptools.pypa.io/en/latest/index.html).

5. update the [LICENSE](./LICENSE)

The License for plugins is always `MIT`. So before proceeding, remember to update the [LICENSE file](./LICENSE) adding the year and your name.

6. update the [README.md file](./README.md)

Doing that, delete everything in this very `README.md` file and describe your project.

7. upload to [PYPI](https://pypi.org/)

As the final step, follow [this guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/) to make your project available on [PYPI](https://pypi.org/).

Also, having a `Github` repo with your code is mandatory to be accepted as an official plugin.

8. request your plugin to be added to the list

After that, open an issue on [github.com/quantum-plugins/plugins-list](https://github.com/quantum-plugins/plugins-list) requesting your plugin to be added. As soon as possible we'll see that and procede with the addition.

## CONGRATS!!!

Now, you have a quantum plugin!!!!

Thank you so much for joining this amazing community🎉🎉🎉