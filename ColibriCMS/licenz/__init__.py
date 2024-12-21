# MODULE = {
#         'jpserver': 1, 
#         'order': 2, 
#         'keysystem': 3
#         }

# import db_ctrl  # @UnresolvedImport
from . import main
# import db_models  # @UnresolvedImport
# import task  # @UnresolvedImport

# try:
#     data = db_ctrl.get_all_row()
#     if data == []:
#         for item in MODULE:
#             db_ctrl.add_row(item, '')
#         data = db_ctrl.get_all_row()
#          
#     if len(data) != len(MODULE):
#         for item in MODULE:
#             data = db_ctrl.get_row(item)
#             if data == None:
#                 db_ctrl.add_row(item, '')
# except:
#     pass