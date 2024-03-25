print("Register to vote, your vote is your power to make a change")

register_party =["ASC", "ATM", "AASD", "ANC", "AGANG SA", "ALJAMA", "ATA", "AZAPO", "APC", "BRA", "BLF", "ZACP", "CPM", "CSA", "COPE", "DA", "DLC", "ECOFORUM", "EFF", "F4SD", "FREE DEMS"]
member_count =[1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000]
def register_party(parties):

    registered_parties = {}
    for party in parties:
        if all(key in party for key in ['party_name', 'reg_number', 'member_count']):
            party_name = party['party_name']
            registered_parties[party_name] = {
                'reg_number': party['reg_number'],
                'member_count': party['member_count']
            }
        else:
            print("Invalid party! skipping registration for this party.")
    return registered_parties


parties_list = [
    {'party_name': 'ASC', 'reg_number': '001', 'member_count': 5300},
    {'party_name': 'ATM', 'reg_number': '002', 'member_count': 40000},
    {'party_name': 'AASD', 'reg_number': '003', 'member_count':1000},
    {'party_name': 'ANC', 'reg_number': '004', 'member_count': 500000},
    {'party_name': 'AGANG SA', 'reg_number': '005', 'member_count': 2000},
    {'party_name': 'ALJAMA', 'reg_number': '006', 'member_count': 34000},
    {'party_name': 'ATA', 'reg_number': '007', 'member_count': 92000},
    {'party_name': 'AZAPO', 'reg_number': '008', 'member_count': 72000},
    {'party_name': 'APC', 'reg_number': '009', 'member_count': 67000},
    {'party_name': 'BRA', 'reg_number': '0010', 'member_count': 6000},
    {'party_name': 'BLF', 'reg_number': '0011', 'member_count': 59000},
    {'party_name': 'ZACP', 'reg_number': '0012', 'member_count': 52000},
    {'party_name': 'CPM', 'reg_number': '0013', 'member_count': 511000},
    {'party_name': 'CSA', 'reg_number': '0014', 'member_count': 1000},
    {'party_name': 'COPE', 'reg_number': '0015', 'member_count': 53000},
    {'party_name': 'DA', 'reg_number': '0016', 'member_count': 54000},
    {'party_name': 'DLC', 'reg_number': '0017', 'member_count': 53000},
    {'party_name': 'ECOFORUM', 'reg_number': '0018', 'member_count': 52000},
    {'party_name': 'EFF', 'reg_number': '0019', 'member_count': 5000000},
    {'party_name': 'F4SD', 'reg_number': '0020', 'member_count': 10000},
    {'party_name': 'FREE DEMS', 'reg_number': '0021', 'member_count': 2000},
    
]
party_info = [{'party_name': 'ASD', 'reg_number': '001', 'member_count': 5300}]
registered_parties = register_party(party_info)
print(registered_parties)
print(parties_list )

def update_voter_info(voter_info, voter_id, name, voting_district, has_voted):

 

    if voter_id in voter_info:
        
        voter_info[voter_id]['name'] = name
        voter_info[voter_id]['voting_district'] = voting_district
        
        if not voter_info[voter_id]['has_voted']:
            voter_info[voter_id]['has_voted'] = has_voted
    else:
       
        voter_info[voter_id] = {
            'name': name,
            'voting_district': voting_district,
            'has_voted': has_voted
        }

    return voter_info


voter_info = {
    'V123': {'name': 'Banele', 'voting_district': 'District A', 'has_voted': False},
    'V456': {'name': 'Banesta', 'voting_district': 'District B', 'has_voted': True}
}

voter_info = update_voter_info(voter_info, 'V123', 'Alice Smith', 'District A', True)
print(voter_info)





