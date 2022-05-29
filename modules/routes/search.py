from flask import Blueprint,request, render_template
from package import search
#[Function] 검색 요청
#[DESC] 클라이언트로 받은 검색 요청 처리
#[TODO] 기능 작성

blueprint = Blueprint("search", __name__, url_prefix='/search')

date = ['202112','202201','202202','202203','202204','202205']
locate = ['36110','11110']

module = search.search(date,locate)
@blueprint.route('/')
def searchIndex():
        return render_template('search.html')

@blueprint.route('/rangeSearch',methods=['GET'])
def rangeSearch():
        filterList = module.filterList
        # index = request.form['index']
        # max = request.form['max'] 
        # min = request.form['min']
        page = "range"
        filter = [None, '']
        wordList = [request.args.get('locateSelect'), request.args.get('courtSelect'), request.args.get('divisionSelect')]
        index = request.args.get('index')
        max = request.args.get('max')
        min = request.args.get('min')
        roomList = None
        time = None
        if(index not in filter and min not in filter and max not in filter ):
                try:
                        if(int(index) > 7):
                                return render_template('search.html',page=page,rangeResult = roomList, filterList = filterList, time = time)
                        else:
                                index = int(index)
                        roomList, time = module.rangeSearch(index, max, min, wordList)
                except:
                        return render_template('search.html',page=page,rangeResult = roomList, filterList = filterList, time = time)

        # roomList = module.rangeSearch(5,2006,1977)
        else:
                index, min, max = 0, 0, 1
                roomList, time = module.rangeSearch(index, max, min, wordList)
        return render_template('search.html',page=page,rangeResult = roomList, filterList = filterList, time = time)



@blueprint.route('/matchSearch', methods=['POST','GET'])
def matchSearch():
        filterList = module.filterList
        page = "match"
        filter = [None, '']
        wordList = [request.args.get('locateSelect'), request.args.get('courtSelect'), request.args.get('divisionSelect')]
        index = request.args.get('index')
        value = request.args.get('value')
        roomList = None
        time = None
        if(index not in filter and value not in filter):

                try:
                        if(int(index) > 7 ):

                                return render_template('search.html',page=page,matchResult = roomList, filterList = filterList, time = time)
                        else:
                                index = int(index)
                except:
                        return render_template('search.html',page=page,matchResult = roomList, filterList = filterList, time = time)
                roomList, time = module.matchSearch(index,value,wordList)

                # roomList = module.matchSearch(5,2004)
        else:
                index, value = 0, 0
                roomList, time = module.matchSearch(index,value,wordList)
        return render_template('search.html',page=page,matchResult = roomList, filterList = filterList, time = time)