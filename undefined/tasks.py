
class _Tasks:
    """The _task_ is the basic object around which many operations in Asana are
    centered. In the Asana application, multiple tasks populate the middle pane
    according to some view parameters, and the set of selected tasks determines
    the more detailed information presented in the details pane."""

    def __init__(self, client=None):
        self.client = client
  
    def create(self, params={}, **options): 
        """Creating a new task is as easy as POSTing to the `/tasks` endpoint
        with a data block containing the fields you'd like to set on the task.
        Any unspecified fields will take on default values.
        
        Every task is required to be created in a specific workspace, and this
        workspace cannot be changed once set. The workspace need not be set
        explicitly if you specify a `project` or a `parent` task instead."""
        
        return self.client.post("/tasks", params, **options)
        
  
    def create_in_workspace(self, workspace, params={}, **options): 
        """Creating a new task is as easy as POSTing to the `/tasks` endpoint
        with a data block containing the fields you'd like to set on the task.
        Any unspecified fields will take on default values.
        
        Every task is required to be created in a specific workspace, and this
        workspace cannot be changed once set. The workspace need not be set
        explicitly if you specify a project or a parent task instead."""
        
        path = "/workspaces/%d/tasks" % (workspace)
        return self.client.post(path, params, **options)
        
  
    def find_by_id(self, task, params={}, **options): 
        """Returns the complete task record for a single task."""
        
        path = "/tasks/%d" % (task)
        return self.client.get(path, params, **options)
        
  
    def update(self, task, params={}, **options): 
        """A specific, existing task can be updated by making a PUT request on the
        URL for that task. Only the fields provided in the `data` block will be
        updated; any unspecified fields will remain unchanged.
        
        When using this method, it is best to specify only those fields you wish
        to change, or else you may overwrite changes made by another user since
        you last retrieved the task.
        
        Returns the complete updated task record."""
        
        path = "/tasks/%d" % (task)
        return self.client.put(path, params, **options)
        
  
    def delete(self, task, params={}, **options): 
        """A specific, existing task can be deleted by making a DELETE request on the
        URL for that task. Deleted tasks go into the "trash" of the user making
        the delete request. Tasks can be recovered from the trash within a period
        of 30 days; afterward they are completely removed from the system.
        
        Returns an empty data record."""
        
        path = "/tasks/%d" % (task)
        return self.client.delete(path, params, **options)
        
  
    def find_by_project(self, projectId, params={}, **options): 
        """Returns the compact task records for all tasks within the given project,
        ordered by their priority within the project."""
        
        path = "/projects/%d/tasks" % (projectId)
        return self.client.get_collection(path, params, **options)
        
  
    def find_by_tag(self, tag, params={}, **options): 
        """Returns the compact task records for all tasks with the given tag."""
        
        path = "/tags/%d/tasks" % (tag)
        return self.client.get_collection(path, params, **options)
        
  
    def find_all(self, params={}, **options): 
        """Returns the compact task records for some filtered set of tasks. Use one
        or more of the parameters provided to filter the tasks returned."""
        
        return self.client.get_collection("/tasks", params, **options)
        
  
    def add_followers(self, task, params={}, **options): 
        """Adds each of the specified followers to the task, if they are not already
        following. Returns the complete, updated record for the affected task."""
        
        path = "/tasks/%d/addFollowers" % (task)
        return self.client.post(path, params, **options)
        
  
    def remove_followers(self, task, params={}, **options): 
        """Removes each of the specified followers from the task if they are
        following. Returns the complete, updated record for the affected task."""
        
        path = "/tasks/%d/removeFollowers" % (task)
        return self.client.post(path, params, **options)
        
  
    def projects(self, task, params={}, **options): 
        """Returns a compact representation of all of the projects the task is in."""
        
        path = "/tasks/%d/projects" % (task)
        return self.client.get_collection(path, params, **options)
        
  
    def add_project(self, task, params={}, **options): 
        """Adds the task to the specified project, in the optional location
        specified. If no location arguments are given, the task will be added to
        the beginning of the project.
        
        `addProject` can also be used to reorder a task within a project that
        already contains it.
        
        Returns an empty data block."""
        
        path = "/tasks/%d/addProject" % (task)
        return self.client.post(path, params, **options)
        
  
    def remove_project(self, task, params={}, **options): 
        """Removes the task from the specified project. The task will still exist
        in the system, but it will not be in the project anymore.
        
        Returns an empty data block."""
        
        path = "/tasks/%d/removeProject" % (task)
        return self.client.post(path, params, **options)
        
  
    def tags(self, task, params={}, **options): 
        """Returns a compact representation of all of the tags the task has."""
        
        path = "/tasks/%d/tags" % (task)
        return self.client.get_collection(path, params, **options)
        
  
    def add_tag(self, task, params={}, **options): 
        """Adds a tag to a task. Returns an empty data block."""
        
        path = "/tasks/%d/addTag" % (task)
        return self.client.post(path, params, **options)
        
  
    def remove_tag(self, task, params={}, **options): 
        """Removes a tag from the task. Returns an empty data block."""
        
        path = "/tasks/%d/removeTag" % (task)
        return self.client.post(path, params, **options)
        
  
    def subtasks(self, task, params={}, **options): 
        """Returns a compact representation of all of the subtasks of a task."""
        
        path = "/tasks/%d/subtasks" % (task)
        return self.client.get_collection(path, params, **options)
        
  
    def add_subtask(self, task, params={}, **options): 
        """Makes an existing task a subtask of another. Returns an empty data block."""
        
        path = "/tasks/%d/subtasks" % (task)
        return self.client.post(path, params, **options)
        
  
    def stories(self, task, params={}, **options): 
        """Returns a compact representation of all of the stories on the task."""
        
        path = "/tasks/%d/stories" % (task)
        return self.client.get_collection(path, params, **options)
        
  
    def add_comment(self, task, params={}, **options): 
        """Adds a comment to a task. The comment will be authored by the
        currently authenticated user, and timestamped when the server receives
        the request.
        
        Returns the full record for the new story added to the task."""
        
        path = "/tasks/%d/stories" % (task)
        return self.client.post(path, params, **options)
        
  