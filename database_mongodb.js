db.user_details.find({})
   .projection({})
   .sort({_id:-1})
   .limit(100)