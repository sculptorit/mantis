import pytest
import random
import string

from model.project import Project


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*2
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Project(project_name=random_string("project", 15), project_description=random_string("descr", 15))
    for i in range(2)
]


@pytest.mark.parametrize("project", testdata, ids=[repr(x) for x in testdata])
def test_del_proj(app, project):
    if len(app.project.get_projects_list()) == 0:
        app.project.create(project)
    old_projects_list = app.project.get_projects_list()
    project_rnd = random.choice(old_projects_list)
    app.project.delete_project(project_rnd)
    new_projects_list = app.project.get_projects_list()
    old_projects_list.remove(project_rnd)
    assert sorted(old_projects_list, key=Project.is_name_empty) == sorted(new_projects_list, key=Project.is_name_empty)
