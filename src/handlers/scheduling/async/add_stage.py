import random

from src import common
from src.handlers.scheduling.scheduling_base import SchedulingBaseHandler
from src.jinja import JINJA_ENVIRONMENT
from src.models.scheduling.round import ScheduleRound
from src.models.scheduling.stage import ScheduleStage


class AddStageHandler(SchedulingBaseHandler):
  def post(self, schedule_version):
    if not self.SetSchedule(int(schedule_version)):
      return
    old_stage = ScheduleStage.get_by_id(self.request.POST['id'])
    is_new_stage = not old_stage

    if old_stage and old_stage.schedule != self.schedule.key:
      return
    stage = old_stage or ScheduleStage(id=self.request.POST['id'])

    stage.schedule = self.schedule.key
    stage.name = self.request.POST['name']
    stage.color_hex = self.request.POST['color']
    stage.timers = int(self.request.POST['timers'])
    if not stage.number:
      max_stage = (ScheduleStage
                     .query(ScheduleStage.schedule == self.schedule.key)
                     .order(-ScheduleStage.number)
                     .get())
      if max_stage:
        stage.number = max_stage.number + 1
      else:
        stage.number = 1
    stage.put()

    template = JINJA_ENVIRONMENT.get_template('scheduling/stages.html')
    stages = (ScheduleStage
                  .query(ScheduleRound.schedule == self.schedule.key)
                  .order(ScheduleRound.number)
                  .fetch())
    if is_new_stage:
      stages.append(stage)
    self.response.write(template.render({
        'c': common.Common(self),
        'stages': stages,
        'new_stage_id': random.randint(2 ** 4, 2 ** 10),
    }))
