using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Xamarin.Forms;
using Firebase.Database;
using Firebase.Database.Query;

namespace EmergingTechs
{
	public partial class MainPage : ContentPage
	{
        public FirebaseClient firebase = new FirebaseClient("https://pruebafirebase-8f87b.firebaseio.com/");
        public List<FirebaseModel> imgs;

        public MainPage()
		{
            InitializeComponent();
		}

        protected async override void OnAppearing()
        {
            base.OnAppearing();
            imgs = await GetAllImg();
            lstImgs.ItemsSource = imgs;
        }
        

        public async Task<List<FirebaseModel>> GetAllImg()
        {

            return (await firebase
              .Child("raspberry")
              .OnceAsync<FirebaseModel>()).Select(item => new FirebaseModel
              {
                  txt = item.Object.txt,
                  img = item.Object.img
              }).ToList();
        }

    }

    public class FirebaseModel
    {
        public string txt { get; set; }
        public string img { get; set; }
    }
}
