from pymongo import MongoClient
import time

db = MongoClient()["db"]
# -------------------------------------------------------------------TEXT_...-------------------------------------------------------------------------------------
t_doc = 'doc'
t_id = '_id'
t_status = 'status'
t_file, t_dir, t_text, t_img, t_parent, t_children, t_name = 'file', 'dir', 'text', 'img', 'parent', 'children', 'nameofdoc'
# SIGN(start) OF THE ELEMENT
sgn_file, sgn_dir, sgn_img, sgn_text = 'file_', 'dir_', 'img_', 'text_'
t_data = 'data'


# -----------------------------------------------------------------------------------------------------------------------------------------------


# CREATE FILE -> RETURN file(collection) name
def create_file(cb: 'Current DataBase', name: 'Name of file'):
    # Get a collection from our db (Create if it's not exist yet)
    fullname = sgn_file + name
    cur_file = db[fullname]

    # Add 1st empty-doc data of thr file (for creation of the collection)
    data = {t_id: t_doc, t_status: t_file}
    cur_file.insert_one(data)

    return fullname


# ADD DATA TO FILE -> Return last input id of the file
def add_one_data_file(cb: 'Current DB', filename, status: 'text / img / file, codes...', nameofdoc,
                      data: 'img bytecode or text..'):
    # Get file(collection) from our DB
    cur_file = db[filename]

    # Generate id for document by current time
    sgn_begin = ''
    if status == t_img:
        sgn_begin = sgn_img
    elif status == t_text:
        sgn_begin = sgn_text
    new_id = sgn_begin + time.strftime("%Y.%m.%d.%H.%M.%S")

    # INSERT NEW DOCUMENT TO CURRENT FILE
    document = {t_id: new_id, t_status: status, t_data: data, t_name: nameofdoc}
    cur_file.insert_one(document)

    return new_id


# GET ALL DATA FROM THE FILE -> RETURN LIST WITH DATA
def get_all_data_file(cb: 'Current DB', filename):
    # Get file(collection) from our DB
    cur_file = db[filename]

    # Get all documents and extract from it status and data for dataTuple
    all_doc = cur_file.find({t_data})
    all_data = []
    for doc in all_doc:
        cur_status = doc[t_status]
        cur_data = doc[t_data]
        all_data.append((cur_status, cur_data))

    return all_data


# DELETE DATA(ONE OR MANY) FROM THE FILE -> RETURN AMOUNT OF THE DELETED DOCUMENTS
def delete_data_file(cb: 'Current DB', filename, id_list: 'list of the id'):
    # Get file(collection) from our DB
    cur_file = db[filename]

    # DELETE ONE OR MANY DOCUMENTS FROM FILE BY IDS
    del_counter = 0
    for id in id_list:
        cur_file.delete_one({t_id: id})
        del_counter += 1

    return del_counter


# FIND SOME DOC BY CLICK


# CREATE DIR -> Return last(first) ID and dir(collection) name
def create_dir(cb: 'Current DataBase', name: 'Name of dir', parent: 'Parent DIR name'):
    # Get a collection from our db (Create if it's not exist yet)
    fullname = sgn_dir + name
    cur_dir = db[fullname]

    # Add 1st empty-doc data of thr dir (for creation of the collection)
    data = {t_id: t_doc, t_status: t_dir, t_parent: parent, t_children: []}
    cur_dir.insert_one(data)

    return fullname


# ADD DATA(child dir) TO DIR -> RETURN NAME/ID OF THE NEW DOCUMENT
def add_one_data_dir(cb: 'Current DB', dirname: 'Parent dir', new_dirname: 'Child dir'):
    # Get PARENT dir(collection) from our DB
    cur_dir = db[dirname]

    # Generate id for document by current time
    new_id = new_dirname

    # UPDATE (ADD NEW CHILD NAME FOR PARENT DOCUMENTATION) LIST OF CHILD_DIR
    doc = cur_dir.find_one({t_id: t_doc})
    upd_doc = doc[t_children].append(new_dirname)
    cur_dir.update_one({t_id: t_doc}, {'$set': {t_children: upd_doc}})

    # INSERT NEW DOCUMENT(CHILD DIR) TO CURRENT FILE(PARENT DIR)
    document = {t_id: new_id, t_parent: dirname}
    cur_dir.insert_one(document)

    return new_id  # THE SAME AS A NAME


# OPEN ALL CHILD DIRECTORIES -> RETURN ALL CHILD_dir NAMES FROM THE DIR
def get_all_from_dir(cb: 'Current DB', dirname: 'Parent directory name'):
    # Get file(collection) from our DB
    cur_dir = db[dirname]

    # Get all documents name list
    documents = cur_dir.find({})
    all_name = [doc[t_id] for doc in documents]

    return all_name


# DELETE ONE / MANY CHILD DIR BY NAME -> RETURN COUNT OF DELETED ELEMENTS
def delete_one_or_many_dir(cb: 'Current DB', dirname: 'Parent directory name', id_list: 'list of the id / name'):
    # Get PARENT dir(collection) from our DB
    cur_dir = db[dirname]

    # Update doc document in parent dir - delete name of current children
    doc = cur_dir.find_one({t_id: t_doc})
    child_list = doc[t_children]
    for del_name in id_list:
        if del_name in child_list: child_list.remove(del_name)
    cur_dir.update_one({t_id: t_doc}, {'$set': {t_children: child_list}})

    # DELETE ONE OR MANY DOCUMENTS FROM FILE BY IDS
    del_counter = 0
    for del_id in id_list:
        cur_dir.delete_one({t_id: del_id})
        del_counter += 1

    return del_counter


# UPDATE ONE CHILD DIR / FILE
def update_one_dir(cb: 'Current DB', dirname: 'Parent directory name', upd_id: 'Name / id of ubdate dir'):
    # Get PARENT dir(collection) from our DB
    cur_dir = db[dirname]

    #
