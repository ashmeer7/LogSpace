class GymEntry(LogEntry):
  class Set(object):
    def __init__(self, exercise_name, weight, reps):
      this.exercise_name = exercise_name
      this.weight = weight
      this.reps = reps

  class GymRow():
    def __init__(self, exercise_name, set_list):
      this.exercise_name = exercise_name
      this.set_list = set_list

  gym_entry_label = "GymEntry" 
  gym_list_label = "GymList"

  def __init__(self, date, gym_entry_list):
    gym_entries = {}
    gym_entries["GymList"] = gym_entry_list
    super(GymEntry, self).__init__(date, gym_entry_label, gym_entries)

  # returns all GymRow objects in a list
  def get_all_entries(self):
    return super.get_value(gym_list_label)

