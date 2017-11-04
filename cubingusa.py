import webapp2

from src import config
from src import handlers
from src.handlers.async.champions_by_year import ChampionsByYearHandler
from src.handlers.async.competitions_us import USCompetitionsHandler
from src.handlers.basic import BasicHandler
from src.handlers.documents import DocumentsHandler
from src.handlers.documents import GetDocumentHandler
from src.handlers.admin.documents import DeleteDocumentHandler
from src.handlers.admin.documents import RestoreDocumentHandler
from src.handlers.admin.documents import UploadDocumentHandler
from src.handlers.edit_user import EditUserHandler
from src.handlers.login import LoginHandler
from src.handlers.login import LoginCallbackHandler
from src.handlers.login import LogoutHandler

app = webapp2.WSGIApplication([
  webapp2.Route('/', handler=BasicHandler('index.html'), name='home'),
  webapp2.Route('/login', handler=LoginHandler, name='login'),
  webapp2.Route('/login_callback', handler=LoginCallbackHandler, name='login_callback'),
  webapp2.Route('/logout', handler=LogoutHandler, name='logout'),
  webapp2.Route('/edit', handler=EditUserHandler, name='edit_user'),
  webapp2.Route('/edit/<user_id:\d+>', handler=EditUserHandler, name='edit_user_by_id'),
  webapp2.Route('/competitions/us', handler=BasicHandler('competitions_us.html'), name='competitions_us'),
  webapp2.Route('/nationals', handler=BasicHandler('nationals.html'), name='competitions_nationals'),
  webapp2.Route('/regional', handler=BasicHandler('index.html'), name='competitions_regional'),
  webapp2.Route('/organizers', handler=BasicHandler('index.html'), name='organizers'),
  webapp2.Route('/about', handler=BasicHandler('about.html'), name='about'),
  webapp2.Route('/about/who', handler=BasicHandler('about_who.html'), name='about_who'),
  webapp2.Route('/about/donations', handler=BasicHandler('donations.html'), name='about_donations'),
  webapp2.Route('/about/documents', handler=DocumentsHandler, name='documents'),
  webapp2.Route('/about/get_document/<document_id:.*>/<document_name:.*>',
                handler=GetDocumentHandler, name='get_document'),
  webapp2.Route('/contact', handler=BasicHandler('index.html'), name='contact'),
  # Async
  webapp2.Route('/async/champions_by_year/<event_id:.*>/<championship_type:.*>/<championship_region:.*>',
                handler=ChampionsByYearHandler),
  webapp2.Route('/async/competitions_us/<year:.*>', handler=USCompetitionsHandler),
  # Admin
  webapp2.Route('/admin/upload_document', handler=UploadDocumentHandler,
                name='upload_document'),
  webapp2.Route('/admin/delete_document/<document_id:.*>', handler=DeleteDocumentHandler,
                name='delete_document'),
  webapp2.Route('/admin/restore_document/<document_id:.*>', handler=RestoreDocumentHandler,
                name='restore_document'),
], config=config.GetAppConfig())
