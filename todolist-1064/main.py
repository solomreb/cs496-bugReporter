#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

bugs = [
    {
        'id': 1,
        'title': u'Bug 1',
        'class': u'Serioius Bug',
        'reporter': u'Joe Smoe',
        'platform': u'OS X',
        'reproducable': False,
        'description': u'This is a description of the bug'
    },
    {
        'id': 2,
        'title': u'Bug 2',
        'class': u'Feature Request',
        'reporter': u'Joe Smoe',
        'platform': u'Windows',
        'reproducable': True,
        'description': u'This is a description of the bug'
    }
]



def make_public_bug(bug):
	new_bug = {}
	for field in bug:
		if field == 'id':
			new_bug['uri'] = url_for('get_bug', bug_id=bug['id'], _external=True)
		else:
			new_bug[field] = bug[field]
	return new_bug

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/api/bugs', methods=['GET'])
def get_bugs():
    return jsonify({'bugs': [make_public_bug(bug) for bug in bug]})

@app.route('/api/bugs/<int:bug_id>', methods=['GET'])
def get_bug(bug_id):
	bugList = [bug for bug in bugs if bug['id'] == bug_id]
	if len(bugList) == 0:
		abort(404)
	return jsonify({'bug': bugList[0]})

@app.route('/api/bugs', methods=['POST'])
def create_bug():
	if not request.json or not 'title' in request.json:
		abort(404)
	bug = {
		'id': bugs[-1]['id'] + 1,
        'title': request.json['title'],
        'class': u'Serioius Bug',
        'reporter': u'Joe Smoe',
        'platform': u'OS X',
        'reproducable': False,
        'description': request.json.get('description', "")
	}
	bugs.append(bug)
	return jsonify({'bug': bug}), 201	

@app.route('/api/bugs/<int:bug_id>', methods=['PUT'])
def update_bug(bug_id):
    bug = [bug for bug in bugs if bug['id'] == bug_id]
    if len(bug) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    bug[0]['title'] = request.json.get('title', bug[0]['title'])
    bug[0]['description'] = request.json.get('description', bug[0]['description'])
    bug[0]['done'] = request.json.get('done', bug[0]['done'])
    return jsonify({'bug': bug[0]})

@app.route('/api/bugs/<int:bug_id>', methods=['DELETE'])
def delete_bug(bug_id):
    bug = [bug for bug in bugs if bug['id'] == bug_id]
    if len(bug) == 0:
        abort(404)
    bugs.remove(bug[0])
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(debug=True)
