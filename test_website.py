import unittest, logging, requests

class TestWebsite(unittest.TestCase):
  
  def test_website_other(self):
    logging.info('Testing......')
    try:
      response = requests.get('https://atg.world/')
      logging.info(f"CONNECTION ESTABLISHED SUCCESFULLY = {response.status_code}")

    except requests.ConnectionError:
      logging.error("FAILED TO ESTABLISH CONNECTION")
      print('Unable to connect to website')
    logging.info('Exiting from testing...')

if __name__ == '__main__':
  logging.basicConfig(level=logging.INFO, filename="logfile.log", format="%(asctime)s : %(message)s", filemode='w')
  unittest.main()
