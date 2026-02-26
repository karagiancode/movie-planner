Μια dekstop εφαρμογη που επιτρέπει σε 2 ή περισσοότερους χρήστες να φτίαχνουν μια λίστα για τις ταινίες που θέλουν να δούνε.

Η εφαρμογή υλοποιήθηκε με την χρήση Python 3.x και Firebase Realtime Database για την live αναναίωση της λίστας οποιουδήποτε χρήστη.
Για το GUI χρησιμοποιήθηκε τυπική χρήση της βιβλιοθήκης CustomTkinter για να είναι ένα οικείο και εύχρηστο περιβάλλον.

Για εγκατάσταση βιβλιοθηκών:
   pip install -r requirements.txt

Για να χρησιμοποιήσει κάποιος την εφαρμογή απαιτήται να δημιουργήσει λογαριασμό στο Firebase

Ρύθμιση Firebase:

  Δημιουργήστε ένα project στο Firebase Console.

  Ενεργοποιήστε τη Realtime Database.

  Κατεβάστε το αρχείο serviceAccountKey.json από τα Project Settings.

  Τοποθετήστε το αρχείο στον κεντρικό φάκελο του project.

  Αντικαταστήστε το databaseURL στο tainies.py με το δικό σας URL.

Για να το τρέξετε χρησιμοποιήστε την εντολή:
    python tainies.py

```bash
   git clone [https://github.com/karagiancode/movie-planner.git](https://github.com/το-όνομά-σου/movie-planner.git)
   cd movie-planner