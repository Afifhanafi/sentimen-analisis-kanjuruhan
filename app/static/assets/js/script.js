$('#table_slangwords').DataTable()


$('#table_stopwords').DataTable()


$('#table_dataset_before').DataTable({
    "deferRender": true,
    "ajax": "/api/dataset-sebelum-tragedi-kanjuruhan",
    "columns": [
        {
            data: null, 
            "render": function (data, type, full, meta) {
                return  meta.row + 1;
            },
            className: 'text-center',
        },
        {
            data: 'created_at',
            className: 'text-center',
        },
        { 
            data: 'username',
            className: 'text-center',
        },
        {
            data: 'raw_tweets',
        },
    ],
})

$('#table_dataset_after').DataTable({
    "deferRender": true,
    "ajax": "/api/dataset-sesudah-tragedi-kanjuruhan",
    "columns": [
        {
            data: null, 
            "render": function (data, type, full, meta) {
                return  meta.row + 1;
            },
            className: 'text-center',
        },
        {
            data: 'created_at',
            className: 'text-center',
        },
        { 
            data: 'username',
            className: 'text-center',
        },
        {
            data: 'raw_tweets',
        },
    ],
})


$('#table_preprocessing').DataTable({
    "deferRender": true,
    "ajax": "/list_dataset/",
    "columns": [
        {
            data: null, 
            "render": function (data, type, full, meta) {
                return  meta.row + 1;
            },
            className: 'text-center',
        },
        {
            data: 'created_at',
            className: 'text-center',
        },
        { 
            data: 'username',
            className: 'text-center',
        },
        {
            data: 'raw_tweets',
        },
    ],
})


$('#Preprocessing_Dataset').click(function() {

	var form_dataArray = $('form').serializeArray();
	var jumlah_dataset = parseInt($('#jumlah_dataset').html());
	
	// validasi data preprocessing
	if(jumlah_dataset > 0 && form_dataArray[0]['name'].trim() == 'proses' && form_dataArray[0]['value'].trim() == 'preprocessing') {
		var content =	"";
		
		$.ajax({
			url         : "/pages/preprocessing/",
			data		: $('form').serialize(),
			type        : "POST",
			dataType	: "json",
			beforeSend: function() {		

				content +=	`
                                <!-- [ breadcrumb ] start -->
                                <div class="page-header">
                                    <div class="page-block">
                                        <div class="row align-items-center">
                                            <div class="col-md-12">
                                                <div class="page-header-title">
                                                    <h5 class="m-b-10"><em>Preprocessing</em></h5>
                                                </div>
                                                <ul class="breadcrumb">
                                                    <li class="breadcrumb-item"><i class="feather icon-home"></i></li>
                                                    <li class="breadcrumb-item"><em>Pages</em></li>
                                                    <li class="breadcrumb-item"><em>Preprocessing</em></li>
                                                </ul>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <!-- [ breadcrumb ] end -->
                    
                                
                                <!-- [ Table Content ] start -->
                                <div class="row">
                    
                                    <!-- [ Dataset Table ] start -->
                                    <div class="col-xl-12" id="infoPreprosessing">
                                        <div class="card text-center">
                                            <div class="card-body">
                                                <h5 class="card-title">Memproses `+ jumlah_dataset +` data, mohon menunggu</h5>
                                                <div class="d-flex justify-content-center" id="loader">
                                                    <button class="btn btn-primary m-2" type="button" disabled="">
                                                        <span class="spinner-border spinner-border-sm" role="status"></span>
                                                        Memuat...
                                                    </button>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                    
                                </div>
							`;
							
				$('#contentPreprocessingData').html(content);
				$("#infoPreprosessing").show();
			},

			success     : function(response) {
				content +=	`
                                <div class="row">

                                    <!-- [ Hasil Preprocessing ] start -->
                                    <div class="col-xl-12">
                                        <div class="card">
                                            <div class="card-header">
                                                <div class="alert alert-success alert-dismissible fade show" role="alert">
                                                    <svg class="bi flex-shrink-0 me-2" width="24" height="24" role="img" aria-label="Success:"><use xlink:href="#check-circle-fill"/></svg>
                                                    Berhasil melakukan <em>preprocessing</em> data dan telah tersimpan dalam basis data
                                                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                                                </div>
                                                <a class="btn btn-success" href="/pages/preprocessing"><i class="fa-solid fa-arrow-left" style="margin-left:-0.3em;"></i> &nbsp;Kembali</a>
                                            </div>

                                            <div class="card-body">
                                                <ul class="nav nav-tabs" id="myTab">
                                                    <li class="nav-item">
                                                        <a href="#Casefolding" class="nav-link active" data-bs-toggle="tab"><em>Case Folding</em></a>
                                                    </li>
                                                    <li class="nav-item">
                                                        <a href="#Cleansing" class="nav-link" data-bs-toggle="tab"><em>Cleansing</em></a>
                                                    </li>
                                                    <li class="nav-item">
                                                        <a href="#Slangwords" class="nav-link" data-bs-toggle="tab"><em>Normalization</em></a>
                                                    </li>
                                                    <li class="nav-item">
                                                        <a href="#StopwordsRemoval" class="nav-link" data-bs-toggle="tab"><em>Stopwords Removal</em></a>
                                                    </li>
                                                    <li class="nav-item">
                                                        <a href="#Stemming" class="nav-link" data-bs-toggle="tab"><em>Stemming</em></a>
                                                    </li>
                                                </ul>
                                                <div class="tab-content">
                                                    <div class="tab-pane fade show active" id="Casefolding">
                                                        <div class="table-responsive">
                                                            <table class="table table-striped w-100" id="table_preprocessing_casefolding" cellspacing="0">
                                                                <thead>
                                                                    <tr>
                                                                        <th class="text-center" width="4%">No.</th>
                                                                        <th class="text-center" width="48%"><em>Tweets Before</em></th>
                                                                        <th class="text-center" width="48%"><em>Tweets After</em></th>
                                                                    </tr>
                                                                </thead>
                                                                <tbody>
							`;
							
				$.each(response.awal_data, function(index) {
					content +=	`
                                                                    <tr>
                                                                        <td class="text-center">`+ ++index +`</td>
                                                                        <td>`+ response.awal_data[--index] +`</td>
                                                                        <td>`+ response.caseFolding_data[index] +`</td>
                                                                    </tr>
                                                                
                            `;
				});
				
                    content +=	`			                    </tbody>
                                                            </table>
                                                        </div>
                                                    </div>

                                                    <div class="tab-pane fade show" id="Cleansing">
                                                        <div class="table-responsive">
                                                            <table class="table table-striped w-100" id="table_preprocessing_cleansing" cellspacing="0">
                                                                <thead>
                                                                    <tr>
                                                                        <th class="text-center" width="4%">No.</th>
                                                                        <th class="text-center" width="48%"><em>Tweets Before</em></th>
                                                                        <th class="text-center" width="48%"><em>Tweets After</em></th>
                                                                    </tr>
                                                                </thead>
							`;



                            
				$.each(response.awal_data, function(index) {
					content +=	`
                                                                    <tr>
                                                                        <td class="text-center">`+ ++index +`</td>
                                                                        <td>`+ response.awal_data[--index] +`</td>
                                                                        <td>`+ response.cleansing_data[index] +`</td>
                                                                    </tr>
                                                                
                            `;
				});
				
                    content +=	`			                    </tbody>
                                                            </table>
                                                        </div>
                                                    </div>

                                                    <div class="tab-pane fade show" id="Slangwords">
                                                        <div class="table-responsive">
                                                            <table class="table table-striped w-100" id="table_preprocessing_slangwords" cellspacing="0">
                                                                <thead>
                                                                    <tr>
                                                                        <th class="text-center" width="4%">No.</th>
                                                                        <th class="text-center" width="48%"><em>Tweets Before</em></th>
                                                                        <th class="text-center" width="48%"><em>Tweets After</em></th>
                                                                    </tr>
                                                                </thead>
							`;


				$.each(response.awal_data, function(index) {
					content +=	`
                                                                    <tr>
                                                                        <td class="text-center">`+ ++index +`</td>
                                                                        <td>`+ response.awal_data[--index] +`</td>
                                                                        <td>`+ response.slangwords_data[index] +`</td>
                                                                    </tr>
                                                                
                            `;
				});
				
                    content +=	`			                    </tbody>
                                                            </table>
                                                        </div>
                                                    </div>

                                                    <div class="tab-pane fade show" id="StopwordsRemoval">
                                                        <div class="table-responsive">
                                                            <table class="table table-striped w-100" id="table_preprocessing_StopwordsRemoval" cellspacing="0">
                                                                <thead>
                                                                    <tr>
                                                                        <th class="text-center" width="4%">No.</th>
                                                                        <th class="text-center" width="48%"><em>Tweets Before</em></th>
                                                                        <th class="text-center" width="48%"><em>Tweets After</em></th>
                                                                    </tr>
                                                                </thead>
							`;


				$.each(response.awal_data, function(index) {
					content +=	`
                                                                    <tr>
                                                                        <td class="text-center">`+ ++index +`</td>
                                                                        <td>`+ response.awal_data[--index] +`</td>
                                                                        <td>`+ response.stopwordsRemoval_data[index] +`</td>
                                                                    </tr>
                                                                
                            `;
				});
				
                    content +=	`			                    </tbody>
                                                            </table>
                                                        </div>
                                                    </div>

                                                    <div class="tab-pane fade show" id="Stemming">
                                                        <div class="table-responsive">
                                                            <table class="table table-striped w-100" id="table_preprocessing_stemming" cellspacing="0">
                                                                <thead>
                                                                    <tr>
                                                                        <th class="text-center" width="4%">No.</th>
                                                                        <th class="text-center" width="48%"><em>Tweets Before</em></th>
                                                                        <th class="text-center" width="48%"><em>Tweets After</em></th>
                                                                    </tr>
                                                                </thead>
							`;


                $.each(response.awal_data, function(index) {
                    content +=	`
                                                                    <tr>
                                                                        <td class="text-center">`+ ++index +`</td>
                                                                        <td>`+ response.awal_data[--index] +`</td>
                                                                        <td>`+ response.stemming_data[index] +`</td>
                                                                    </tr>
                                                                
                            `;
                });
                
                    content +=	`			                    </tbody>
                                                            </table>
                                                        </div>
                                                    </div>

                            `;



                    content +=	`
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                `;

                
				
				$('#contentPreprocessingData').html(content);
				
                $("#infoPreprosessing").remove();


				$('#table_preprocessing_casefolding').DataTable();
				$('#table_preprocessing_cleansing').DataTable();
				$('#table_preprocessing_slangwords').DataTable();
				$('#table_preprocessing_StopwordsRemoval').DataTable();
				$('#table_preprocessing_stemming').DataTable();
				$('#table_preprocessing_token').DataTable();
				
				$('body').removeClass('modal-open');
				$('body').removeAttr("style");
                
				$('#table_preprocessing_casefolding th').removeAttr("style");
				$('#table_preprocessing_cleansing th').removeAttr("style");
				$('#table_preprocessing_slangwords th').removeAttr("style");
				$('#table_preprocessing_StopwordsRemoval th').removeAttr("style");
				$('#table_preprocessing_stemming th').removeAttr("style");
				$('#table_preprocessing_token th').removeAttr("style");

				$('.modal-backdrop').remove();
			},
			error     : function(x) {
				console.log(x.responseText);
			}
		});
	} 
	else {
		console.log("error")
	}
});


var table_labelling = $('#table_labelling').DataTable({
	"deferRender": true,
	"ajax": "/list_dataset/",
	"columns": [
		{
			data: null,
            className: 'text-center',
			"render": function (data, type, full, meta) {
				return  meta.row + 1;
			}
		},
        {
			data: 'created_at',
            className: 'text-center'
	 	},
        { 
            data: 'username',
            className: 'text-center'
        },
		{
			data: 'raw_tweets',
			className: 'text-left'
	 	},
         { 
            data: null,
            className: 'text-center',
			"render": function (data, type, full, meta) {
                if (data.label == "Positif"){
                    return `
                        <select name="label_data" id="opsi_label`+ data.id +`" class="btn btn-success">
                            <option value="`+ data.label +`" selected>`+data.label+`</option>
                            <option value="Negatif">Negatif</option>
                        </select>
                    `;
                }else{
                    return `
                        <select name="label_data" id="opsi_label`+ data.id +`" class="btn btn-danger">
                            <option value="`+ data.label +`" selected>`+data.label+`</option>
                            <option value="Positif">Positif</option>
                        </select>
                    `;
                }
			},
        }
	],
});


$('#table_labelling tbody').on('change', 'select[name="label_data"]', function () {
	var data = table_labelling.row($(this).parents('tr')).data();
	id = data['id'];
	value = $(this).find(":selected").text();

    if (value == "Positif") {
        $('#opsi_label'+id).removeClass('btn btn-danger')
        $('#opsi_label'+id).addClass('btn btn-success')
    }else{
        $('#opsi_label'+id).removeClass('btn btn-success')
        $('#opsi_label'+id).addClass('btn btn-danger')
    }
	
	$.ajax({
		url         : "/pages/pelabelan/",
		data		: {'id': id, 'value': value},
		type        : "POST",
		dataType	: "json",
		// success     : function(response) {
		// 	console.log(response);
		// },
		// error     : function(x) {
		// 	console.log(x.responseText);
		// }
	});
});


$('#uji_Dataset').click(function() {

	var totalSplit = parseInt($('#totalSplit').html());
	
	if(totalSplit > 0) {
		var content =	"";
		
		$.ajax({
			url         : "/pages/pengujian/",
			data		: $('form').serialize(),
			type        : "POST",
			dataType	: "json",
			beforeSend: function() {		

				content +=	`
                                <!-- [ breadcrumb ] start -->
                                <div class="page-header">
                                    <div class="page-block">
                                        <div class="row align-items-center">
                                            <div class="col-md-12">
                                                <div class="page-header-title">
                                                    <h5 class="m-b-10">Pengujian</h5>
                                                </div>
                                                <ul class="breadcrumb">
                                                    <li class="breadcrumb-item"><i class="feather icon-home"></i></li>
                                                    <li class="breadcrumb-item"><em>Pages</em></li>
                                                    <li class="breadcrumb-item">Pengujian</li>
                                                </ul>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <!-- [ breadcrumb ] end -->
                    
                                
                                <!-- [ Table Content ] start -->
                                <div class="row">
                    
                                    <!-- [ Dataset Table ] start -->
                                    <div class="col-xl-12" id="infoTesting">
                                        <div class="card text-center">
                                            <div class="card-body">
                                                <h5 class="card-title">Memproses data sampel, mohon menunggu</h5>
                                                <div class="d-flex justify-content-center" id="loader">
                                                    <button class="btn btn-primary m-2" type="button" disabled="">
                                                        <span class="spinner-border spinner-border-sm" role="status"></span>
                                                        Memuat...
                                                    </button>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                    
                                </div>
							`;
							
				$('#contentTestingData').html(content);
				$("#infoTesting").show();
			},

			success     : function(response) {
				content +=	`
                                <div class="row">

                                    <!-- [ Hasil Pengujian ] start -->
                                    <div class="col-xl-12">
                                        <div class="card">
                                            <div class="card-header">
                                                <div class="alert alert-success alert-dismissible fade show" role="alert">
                                                    <svg class="bi flex-shrink-0 me-2" width="24" height="24" role="img" aria-label="Success:"><use xlink:href="#check-circle-fill"/></svg>
                                                    Berhasil melakukan pembagian dan pengujian data
                                                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                                                </div>
                                                <a class="btn btn-success" href="/pages/pengujian"><i class="fa-solid fa-arrow-left" style="margin-left:-0.3em;"></i> &nbsp;Kembali</a>
                                            </div>

                                            <div class="card-body">
                                                <ul class="nav nav-tabs" id="myTab">
                                                    <li class="nav-item">
                                                        <a href="#DataLatih" class="nav-link active" data-bs-toggle="tab">Data Latih</a>
                                                    </li>
                                                    <li class="nav-item">
                                                        <a href="#DataUji" class="nav-link" data-bs-toggle="tab">Data Uji</a>
                                                    </li>
                                                    
                                                </ul>
                                                <div class="tab-content">

                                                    <div class="tab-pane fade show active" id="DataLatih">
                                                        <div class="table-responsive">
                                                            <table class="table table-striped w-100" id="table_dataLatih" cellspacing="0">
                                                                <thead>
                                                                    <tr>
                                                                        <th class="text-center" width="4%">No.</th>
                                                                        <th class="text-center" width="83%">Tweets </th>
                                                                        <th class="text-center" width="13%">Label</th>
                                                                    </tr>
                                                                </thead>
                                                                <tbody>
                                                           
							`;
							
				$.each(response.X_train, function(index) {
					content +=	`
                                                                    <tr>
                                                                        <td class="text-center">`+ ++index +`</td>
                                                                        <td>`+ response.X_train[--index] +`</td>
                                                                        <td class="text-center" width="20%">`+ response.y_train[index] +`</td>
                                                                    </tr>
                            `;                          
				});
				
                    content +=	`			                    </tbody>
                                                            </table>
                                                        </div>
                                                    </div>

                                                    <div class="tab-pane fade show" id="DataUji">
                                                        <div class="table-responsive">
                                                            <table class="table table-striped w-100" id="table_dataUji" cellspacing="0">
                                                                <thead>
                                                                    <tr>
                                                                        <th class="text-center" width="4%">No.</th>
                                                                        <th class="text-center" width="56%">Tweets</th>
                                                                        <th class="text-center" width="10%">Label (<em>Actual</em>)</th>
                                                                        <th class="text-center" width="10%">Label (<em>Predict</em>)</th>
                                                                    </tr>
                                                                </thead>
                                                                <tbody>

							`;



                            
				$.each(response.X_test, function(index) {
					content +=	`
                                                                    <tr>
                                                                        <td class="text-center">`+ ++index +`</td>
                                                                        <td>`+ response.X_test[--index] +`</td>
                                                                        <td class="text-center" width="15%">`+ response.y_test[index] +`</td>
                                                                        <td class="text-center" width="15%">`+ response.predict[index] +`</td>
                                                                    </tr>
                                                                
                            `;
				});
				
                    content +=	`			              
                                                                </tbody>
                                                            </table>
                                                        </div>
                                                    </div>
                                                                
                                                </div>
                                            </div>
                                        </div>

                                    </div>
                                    <!-- [ Hasil Pengujian ] start -->
                                </div>

                                <div class="row">
                                    <div class="col-xl-12">
                                        <div class="card">

                                            <div class="card-header text-center">
                                                <h3>Tabel <em>Confusion Matrix</em></h3>
                                            </div>
                                            <div class="card-body">
                                                <div class="d-flex justify-content-center container">
                                                    <table class="table table-bordered text-center text-muted">
                                                        
                                                        <tbody>
                                                            <tr>
                                                                <td rowspan="2" class="align-middle" width="25%"><b>Data Aktual</b></td>
                                                                <td colspan="2" class="align-middle" width="50%"><b>Data Prediksi</b></td>
                                                                <td rowspan="2" class="align-middle" width="25%"><b>Total</b></td>
                                                            </tr>
                                                            <tr>
                                                                <td class="align-middle"><b>Positif</b></td>
                                                                <td class="align-middle"><b>Negatif</b></td>
                                                            </tr>
                                                            <tr>
                                                                <td class="align-middle"><b>Positif</b></td>
                                                                <td class="bg-primary">
                                                                    <h5 class="text-light">`+ response.cmatrix['tpositif'] +`</h5>
                                                                    <small class="text-light">TP(<em>True Positive</em>)</small>
                                                                </td>
                                                                <td>
                                                                    <h5 class="text-dark">`+ response.cmatrix['fnegatif'] +`</h5>
                                                                    <small>FN (<em>False Negatif</em>)</small>
                                                                </td>
                                                                <td>
                                                                    <h5 class="text-dark">`+ (parseInt(response.cmatrix['tpositif']) + parseInt(response.cmatrix['fnegatif'])) +`</h5>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td class="align-middle"><b>Negatif</b></td>
                                                                <td>
                                                                    <h5 class="text-dark">`+ response.cmatrix['fpositif'] +`</h5>
                                                                    <small>FP (<em>False Positive</em>)</small>
                                                                </td>
                                                                <td class="bg-primary">
                                                                    <h5 class="text-light">`+ response.cmatrix['tnegatif'] +`</h5>
                                                                    <small class="text-light">TN (<em>True Negatif</em>)</small>
                                                                </td>
                                                                <td>
                                                                    <h5 class="text-dark">`+ (parseInt(response.cmatrix['fpositif']) + parseInt(response.cmatrix['tnegatif'])) +`</h5>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td class="align-middle"><b>Total</b></td>
                                                                <td>
                                                                    <h5 class="text-dark">`+ (parseInt(response.cmatrix['tpositif']) + parseInt(response.cmatrix['fpositif'])) +`</h5>
                                                                </td>
                                                                <td>
                                                                    <h5 class="text-dark">`+ (parseInt(response.cmatrix['fnegatif']) + parseInt(response.cmatrix['tnegatif'])) +`</h5>
                                                                </td>
                                                                <td class="bg-info">
                                                                    <h5 class="text-light">`+ (parseInt(response.cmatrix['tpositif']) + parseInt(response.cmatrix['tnegatif']) + parseInt(response.cmatrix['fpositif'])+ parseInt(response.cmatrix['fnegatif'])) +`</h5>
                                                                </td>
                                                            </tr>
                                                        </tbody>

                                                    </table>
                                                    

                                                </div>
                                            </div>

                                            <div class="card-footer text-center">
                                                <h3>Detail Perhitungan Evaluasi</h3>
                                            </div>
                                            <div class="card-body">
                                                <table class="table table-bordered table-sm">
                                                    <tbody>
                                                        <tr>
                                                            <th class="text-right" width="33.33%"><span class="h6">Akurasi</span></th>
                                                            <th class="text-right" width="33.33%"><span class="h6">Presisi</span></th>
                                                            <th class="text-right" width="33.33%"><span class="h6"><em>Recall</em></span></th>
                                                        </tr>
                                                        <tr>
                                                            <td><span class="h6 text-dark">= (( TP + TN ) / ( TP + TN + FP + FN )) x 100% </span></td>
                                                            <td><span class="h6 text-dark">= (((TP / ( TP + FP )) + (TN / ( TN + FN ))) / 2) x 100% </span></td>
                                                            <td><span class="h6 text-dark">= (((TP / ( TP + FN )) + (TN / ( TN + FP ))) / 2) x 100% </span></td>
                                                        </tr>
                                                        <tr>
                                                            <td><span class="h6 text-dark">= ((`+ response.cmatrix['tpositif'] +` + `+ response.cmatrix['tnegatif'] +`) / (`+ response.cmatrix['tpositif'] +` + `+ response.cmatrix['tnegatif'] +` + `+ response.cmatrix['fpositif'] +` + `+ response.cmatrix['fnegatif'] +`)) x 100%</span></td>
                                                            <td>
                                                                <span class="h6 text-dark">
                                                                    = (((`+ response.cmatrix['tpositif'] +` / ( `+ response.cmatrix['tpositif'] +` + `+ response.cmatrix['fpositif'] +` )) + (`+ response.cmatrix['tnegatif'] +` / ( `+ response.cmatrix['tnegatif'] +` + `+ response.cmatrix['fnegatif'] +` ))) / 2) x 100%
                                                                    <br>
                                                                    = ((`+ response.cmatrix['precision_p'] +`) + (`+ response.cmatrix['precision_n'] +`) / 2) x 100%
                                                                </span>
                                                            </td>
                                                            <td>
                                                                <span class="h6 text-dark">
                                                                    = (((`+ response.cmatrix['tpositif'] +` / ( `+ response.cmatrix['tpositif'] +` + `+ response.cmatrix['fnegatif'] +` )) + (`+ response.cmatrix['tnegatif'] +` / ( `+ response.cmatrix['tnegatif'] +` + `+ response.cmatrix['fpositif'] +` ))) / 2) x 100% 
                                                                    <br>
                                                                    = ((`+ response.cmatrix['recall_p'] +`) + (`+ response.cmatrix['recall_n'] +`) / 2) x 100%
                                                                </span>
                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <td><span class="h6 text-dark">= `+ Math.round(response.cmatrix['accuration'] * 100) +`%</span></td>
                                                            <td><span class="h6 text-dark">= `+ Math.round(response.cmatrix['precision_rate'] * 100) +`%</span></td>
                                                            <td><span class="h6 text-dark">= `+ Math.round(response.cmatrix['recall_rate'] * 100) +`%</span></td>
                                                        </tr>

                                                    </tbody>
                                                </table>
                                            </div>
                                        </div>

                                        

                                    </div>
                                </div>

                                <div class="row">
                                    <div class="col-xl-12">
                                        <div class="card">

                                            <div class="card-header text-center">
                                                <h3>Visualisasi Hasil Prediksi</h3>
                                            </div>
                                            <div class="card-body">
                                                <div class="chartBox">
                                                    <canvas id="pieChart"></canvas>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>


                                <script>
                                    const ctx = document.getElementById('pieChart').getContext('2d');
                                    const pieChart = new Chart(ctx, {
                                        type: 'pie',
                                        data: {
                                            labels: [
                                            'Sentimen Positif',
                                            'Sentimen Negatif',
                                            ],
                                            datasets: [{
                                            label: 'My First Dataset',
                                            data: [`+ response.cmatrix['total_p'] +`, `+ response.cmatrix['total_n'] +`],
                                            backgroundColor: [
                                                'rgb(54, 162, 235)',
                                                'rgb(255, 99, 132)',
                                            ],
                                            hoverOffset: 1
                                            }]
                                        },
                                        options: {
                                            maintainAspectRatio: false,
                            
                                            
                                        }
                                    });
                                </script>
							`;
				

				$('#contentTestingData').html(content);
				
                $("#infoTesting").remove();


				$('#table_dataLatih').DataTable();
				$('#table_dataUji').DataTable();
				
				$('body').removeClass('modal-open');
				$('body').removeAttr("style");
                
				$('#table_dataLatih th').removeAttr("style");
				$('#table_dataUji th').removeAttr("style");

				$('.modal-backdrop').remove();
			},
			error     : function(x) {
				console.log(x.responseText);
			}
		});
	} 
	else {
		console.log("Error")
	}
});
