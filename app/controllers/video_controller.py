from app import api, db
from flask_restful import reqparse, Resource, abort
from app.models.video_model import VideoModel

class VideoController(Resource):
    def __init__(self):
        super().__init__()
        self.video_args = reqparse.RequestParser()
        self.video_args.add_argument('name', type=str, help="Name of the video is required", required=True)
        self.video_args.add_argument('views', type=int, help="Number of views of the video is required", required=True)
        self.video_args.add_argument('likes', type=int, help="Number of likes of the video is required", required=True)
        self.video_model = VideoModel()
    
    def abort_if_not_exists(self, id:int):
        videos = self.video_model.select_all()
        if id not in videos:
            abort(404, message="Video id is not valid")

    def abort_if_exists(self, id:int):
        videos = self.video_model.select_all()
        if id in videos:
            abort(409, message="Video id already exists")

    def get(self, id):
        self.abort_if_not_exists(id)
        res_all = self.video_model.select_all()
        res = self.video_model.select(id)
        return {
            "result": res,
            "all-data": res_all
        }, 200

    def post(self, id):
        self.abort_if_exists(id)
        args = self.video_args.parse_args()
        self.video_model.insert(args['name'], args['views'], args['likes'])
        return '', 204
    
    def put(self, id):
        self.abort_if_not_exists(id)
        args = self.video_args.parse_args()
        self.video_model.update(id, args['name'], args['views'], args['likes'])
        return '', 204

    def delete(self, id):
        self.abort_if_not_exists(id)
        self.video_model.delete(id)
        return ('', 204)

api.add_resource(VideoController, '/video/<int:id>')