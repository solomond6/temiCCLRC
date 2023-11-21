1. select distinct ins.name, ins.phone from inspection_parcel insp join inspectors ins on ins.id = insp.inspection_id join parcels p on p.id = insp.parcel_id where p.ppn ='812-12-027' group by ins.name;

2. select sum(ins.cost_per_parcel) from inspection_parcel insp join inspectors inst on inst.id = insp.inspection_id join inspections ins on ins.id = ins.inspector join parcels p on p.id = insp.parcel_id WHERE instr(p.address, 'East Cleveland')

3. select * from parcels where id not in (select insp.parcel_id from inspection_parcel insp join inspections ins on ins.id = insp.inspection_id where ins.date > '2023-01-01');