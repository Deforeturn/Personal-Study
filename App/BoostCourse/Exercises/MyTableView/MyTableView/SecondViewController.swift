//
//  SecondViewController.swift
//  MyTableView
//
//  Created by Deforeturn on 1/22/22.
//

import UIKit

class SecondViewController: UIViewController {
    var reciveStr:String?
    @IBOutlet var viewLabel:UILabel?
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        viewLabel?.text = reciveStr
    }
    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}
