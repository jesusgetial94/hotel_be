from authApp.models.account         import Account
from authApp.models.transactions    import Transactions
from rest_framework                 import serializers

class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = ['account_origin', 'account_destiny', 'amount', 'register_date', 'note']
    def to_representation(self, obj):
        account_origin = Account.objects.get(id=obj.account_origin)
        account_destiny = Account.objects.get(id=obj.account_destiny)
        transaction = Transactions.objects.get(id=obj.id)
        return {
            'id'            : transaction.id,
            'amount'        : transaction.amount,
            'register_date' : transaction.register_date,
            'note'          : transaction.note,
            'account_origin': {
                'id'                : account_origin.id,
                'balance'           : account_origin.balance,
                'lastChangeDate'    : account_origin.lastChangeDate,
                'isActive'          : account_origin.isActive
            },
            'account_destiny': {
                'id'                : account_destiny.id,
                'balance'           : account_destiny.balance,
                'lastChangeDate'    : account_destiny.lastChangeDate,
                'isActive'          : account_destiny.isActive
            },
        }
