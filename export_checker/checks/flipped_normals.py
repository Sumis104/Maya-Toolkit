from export_checker.base_check import BaseCheck
import maya.cmds as cmds

class FlippedNormalsCheck(BaseCheck):

    name = "法線の反転"
    category = "メッシュ"
    severity = "error"
    description = "メッシュの法線が反転しています。"
    can_fix = True

    def check(self, targets):
        for mesh in targets:
            faces = self._get_face_vertices(mesh)
            print(mesh, len(faces))


    def _get_face_vertices(self, mesh_name):
        lines = cmds.polyInfo(mesh_name, faceToVertex=True)
        faces = []
        for line in lines:
            parts = line.split()[2:]  
            vertex_ids = [int(x)for x in parts]      
            faces.append(vertex_ids)
        return faces
        
