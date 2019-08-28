from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from IPy import IP
from flask import jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/ipmask', methods=['GET', 'POST'])
def ip_mask():
    a = request.values['ip']
    b = request.values['bits']
    ips = IP('%s/%s' % (a, b), make_net=1)
    uip = ips.len()
    snm = str(ips.netmask())
    nwadr = str(ips[0])
    fiuip = str(ips[1])
    lauip = str(ips[uip-1])
    broip = str(ips.broadcast())
    return jsonify({"uip": uip, "snm": snm, "nwadr": nwadr, "fiuip": fiuip, "lauip": lauip, "broip": broip})


@app.route('/ipnet', methods=['GET', 'POST'])
def ip_net():
    a = '0.0.0.0'
    b = request.values['bits2']
    ips = IP('%s/%s' % (a, b), make_net=1)
    dec10 = str(ips.netmask())
    hex16 = str(ips.netmask().strHex())
    return jsonify({"dec10": dec10, "hex16": hex16})

# @app.route('/', methods=['GET', 'POST'])
# def ip_mask():
#     if request.method == "POST":
#         a = request.form['ip']
#         b = request.form['bits']
#         ips = IP('%s/%s' % (a, b), make_net=1)
#         uip = ips.len()
#         snm = ips.netmask()
#         nwadr = ips[0]
#         fiuip = ips[1]
#         lauip = ips[uip-1]
#         broip = ips.broadcast()
#         return render_template('index.html', uip=uip, snm=snm,nwadr=nwadr,fiuip=fiuip,lauip=lauip, broip=broip)
#     return render_template('index.html')

# @app.route('/ip_mask', methods=['GET', 'POST'])
# def ip_mask2():
#     if request.method == "POST":
#         a = request.form['ip2']
#         b = 6
#         return render_template('index.html', snm = b)
#     return render_template('index.html')


if __name__ == "__main__":
    app.run()
