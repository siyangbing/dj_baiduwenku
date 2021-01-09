from django.shortcuts import render, HttpResponse
from django.http import StreamingHttpResponse,FileResponse,Http404
from django.utils.encoding import escape_uri_path
import os
from dj_baiduwenku.settings import BASE_DIR

from bdwk.download_tools.download_doc_ppt_bdwk import StartChrome


def download_doc(request):
    html_path = os.path.join(BASE_DIR,"templates/bdwk.html")
    return render(request, html_path)

# def wait_hl(request):
#     html_path = os.path.join(BASE_DIR, "templates/test.html")
#     # return (render(request, html_path))
#     request.encoding = 'utf-8'
#     if 'doc_url' in request.GET and request.GET['doc_url']:
#         url = request.GET['doc_url']
#         message = '你搜索的内容为: ' + request.GET['doc_url']
#     else:
#         message = '你提交了空表单'
#         url=""
#
#     html_path = os.path.join(BASE_DIR, "templates/test.html")
#     return render(request, html_path,{"url_path":url})

# Create your views here.
def file_down(request):
    """
    下载压缩文件
    :param request:
    :param id: 数据库id
    :return:
    """
    html_path =os.path.join(BASE_DIR,"templates/test.html")
    # return (render(request, html_path))
    request.encoding = 'utf-8'
    if 'doc_url' in request.GET and request.GET['doc_url']:
        url = request.GET['doc_url']
        message = '你搜索的内容为: ' + request.GET['doc_url']
    else:
        message = '你提交了空表单'

    # url = "https://wenku.baidu.com/view/4410199cb0717fd5370cdc2e.html?fr=search"
    start_chrome = StartChrome(url)
    download_path = start_chrome.create_ppt_doc()
    print("download_path {}".format(download_path))
    file_path = download_path
    file_name = download_path.split("/")[-1]  # 文件名
    # file_path = "/home/db/PycharmProjects/dj_baiduwenku/download_files/doc/ppt.docx"
    # file_name = file_path.split("/")[-1]  # 文件名
    print("file_name {}".format(file_name))

    try:
        response = FileResponse(open(file_path, 'rb'))
        response['content_type'] = "application/octet-stream"
        response['Content-Disposition'] = 'attachment; filename={}'.format(escape_uri_path(file_name))
        return response
    except Exception:
        raise Http404
