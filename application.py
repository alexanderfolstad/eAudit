from flask import Flask, render_template, request, jsonify
from scripts import getAuditData



app = Flask(__name__)


@app.route('/')
def home():
    # Pick up POST
    try:
        outletid = request.args.get('outletid')
        period = request.args.get('period')
        outlet = getAuditData.get_OutletName(outletid)
        audits = getAuditData.get_Audit(outletid, period)
    except:
        outlet = 0
        period = 0
        outletid = 0
        audits = ['0']

    # Request Outlet and Audit data
    return render_template("index.html", outlet = outlet, period = period, audits = audits, outletid = outletid)

@app.route('/process', methods=['POST'])
def process():
    outlet = request.form['outlet']
    period = request.form['period']
    sku = request.form['sku']
    instock = request.form['instock']
    onshelf = request.form['onshelf']

    print(outlet)
    print(period)
    print(sku)
    print(instock)
    print(onshelf)
    getAuditData.insert_Audit(outlet, period, sku, instock, onshelf)

    if instock and onshelf:
        outlet = outlet

        return jsonify({'outlet' : outlet})

    return jsonify({'error' : 'Missing data!'})


if __name__ == '__main__':
    app.run()