from flask import Blueprint,request, render_template
from package import search
#[Function] 검색 요청
#[DESC] 클라이언트로 받은 검색 요청 처리
#[TODO] 기능 작성

blueprint = Blueprint("search", __name__, url_prefix='/search')

module = search.search('202203')
@blueprint.route('/')
def searchIndex():
        return render_template('search.html')

@blueprint.route('/rangeSearch',methods=['GET'])
def rangeSearch():

        # index = request.form['index']
        # max = request.form['max'] 
        # min = request.form['min']
        index = request.args.get('index')
        max = request.args.get('max')
        min = request.args.get('min')
        roomList = None
        if(index != None and max != None and min != None):
                if(int(index) > 5):
                        roomList = None
                        return render_template('search.html',index = 1,rangeResult = roomList)
                else:
                        index = int(index)
                roomList = module.rangeSearch(index, max, min)

        # roomList = module.rangeSearch(5,2006,1977)
        return render_template('search.html',index = 1,rangeResult = roomList)


@blueprint.route('/matchSearch', methods=['POST','GET'])
def matchSearch():
        
        index = request.args.get('index')
        value = request.args.get('value')
        roomList = None
        if(index != None and value != None):

                if(int(index) > 5):
                        roomList = None
                        return render_template('search.html',index = 1,matchResult = roomList)
                else:
                        index = int(index)

                roomList = module.matchSearch(index,value)

                # roomList = module.matchSearch(5,2004)
        return render_template('search.html',index = 2,matchResult = roomList)