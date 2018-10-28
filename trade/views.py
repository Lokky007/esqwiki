from django.shortcuts import render
from forms import TradeNewSell

# Create your views here.
def index(request):
    return render(request, 'trade_base.html',
                  {
                      'TradeNewSell': TradeNewSell(initial={'tradeType': '1'})
                  })